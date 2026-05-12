'''
Script with classes and functions to check ands fix the following aspects of a Modelica model:
- Documentation generation
- Documentation review
- Code comprehension
- Code generation
'''
import os
import re
import regex
import pandas as pd
from OMPython import OMCSessionZMQ
from claude import ClaudeDepotLLM
from search import strip_annotations

class ModuleCheck:
    '''
    A class to check and fix various aspects of a Modelica model.
    '''
    def __init__(self, model, base_url, api_key, lib_root, run_api_calls: bool = True):
        '''Initialize the ModuleCheck class with the necessary parameters and load the CDL naming
        rules.'''
        self.cdl_naming_rules = os.path.join(os.getcwd(), 'cdl_naming_rules.md')
        self.doc_rules = os.path.join(os.getcwd(), 'compact_documentation_rules.md')
        self.lib_root = lib_root
        self.omc = OMCSessionZMQ()
        self.setup_omc()
        self.rules_files_contents = []
        for file in [self.cdl_naming_rules]:
            if os.path.exists(file):
                with open(file, 'r', encoding='utf-8') as f:
                    self.rules_files_contents.append(f.read())
            else:
                print(f"Warning: {file} not found. Skipping.")
        self.doc_rules_contents = []
        if os.path.exists(self.doc_rules):
            with open(self.doc_rules, 'r', encoding='utf-8') as f:
                self.doc_rules_contents.append(f.read())
        else:
            raise Exception(f"Warning: {self.doc_rules} not found. Skipping.")
        
        if run_api_calls:
            load_message = f"These are the rules for analyzing the list of variable names I will input\
            in the next prompt. I need you to flag any variable names that are not meeting the CDL naming\
            rules. Please confirm the if you can read the rules. Here are the rules:\n{self.rules_files_contents}"
            self.llm = ClaudeDepotLLM(model, base_url, api_key, '')
            # result = self.llm.invoke(load_message)
            # if 'error' in result:
            #     raise Exception(f"Error loading rules: {result}")
            # else:
            #     print(f"Rules loaded successfully: {result}")

    def analyze_variable_names(self, variables_df:pd.DataFrame):
        '''
        Analyze the list of variable names in the Modelica code and flag any that do not meet the CDL naming rules.
        '''
        # Read the Modelica file and extract variable names
        # with open(filepath, 'r') as f:
        #     model_code = f.read()
        # cleaned = re.sub(r'(?s)model.*?(\n  .*?(?:equation|algorithm).*?end.*?;)', r'\1', model_code)

        df_md = variables_df.to_markdown(index=False)

        analysis_message = f"These are the rules for analyzing the list of variable names I will input\
            in the next prompt. I need you to flag any variable names that are not meeting the CDL naming\
            rules. Please confirm the if you can read the rules. Here are the rules:\n{self.rules_files_contents}\n\n"+\
            f"Here is a table of Modelica variables that includes the variable\
            names alongwith their comments:\n{df_md}\n Please analyze the variable names based\
            on the CDL naming rules I provided earlier and check if they are an accurate representation\
            of the information in the comments. Flag any variable names that do not meet the\
            rules and explain why. Return your analysis in a tabular format with columns for the variable\
            name, the issue identified, and the suggested correction for the variable names that have an issue."
        result = self.llm.invoke(analysis_message)
        return result

    def setup_omc(self):
        """
        Initialize an OpenModelica OMC session and load base libraries.
        Must be called before compiling or simulating models.
        """
        # Load standard Modelica library
        error_modelica = self.omc.sendExpression('loadModel(Modelica)')
        success_modelica = 'error' not in str(error_modelica).lower()
        print("✅ Success loading Modelica:", success_modelica)
        print("📄 Modelica load message:\n", error_modelica)

        # Load Buildings library
        self.load_model('Buildings')

    def load_model(self, modelica_package_tree_path):
        """
        Load a Modelica model into the OMC session.
        """
        model_path = os.path.join(self.lib_root, *modelica_package_tree_path.split('.')) + '.mo'
        if not os.path.exists(model_path):
            model_path = os.path.join(self.lib_root, *modelica_package_tree_path.split('.'), 'package') + '.mo'
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model file not found for {modelica_package_tree_path}")
        error_load = self.omc.sendExpression(f'loadFile("{model_path.replace("'",'').replace('\\','/')}")')
        success_load = 'error' not in str(error_load).lower()
        print(f"✅ Success loading model {modelica_package_tree_path}:", success_load)
        if not success_load:
            raise RuntimeError(f"Failed to load model at {modelica_package_tree_path}. Check the OMC error message for details: {error_load}")
        print("📄 Model load message:\n", error_load)

    def parse_model_variables(self, modelica_package_tree_path, complete_set: bool = False):
        '''Parse the variable declarations of a Modelica model and return a structured representation of its
        components and their relationships. This function uses the OMC session to query the model
        structure and extract relevant information about its components, connections, and behavior.
        The output is a structured representation that can be used for further analysis or transformation.'''
        list_outputs = self.omc.sendExpression(f'getComponentsTest({modelica_package_tree_path})')
        variable_df = pd.DataFrame(columns=['name', 'className', 'comment'])

        index_counter = 0
        for output in list_outputs:
            record_variable = False
            class_name = output['className']
            if class_name.startswith('Buildings.Controls.OBC.CDL.Interfaces'):
                record_variable = True
                variable_df.loc[index_counter, 'type'] = 'interface'
            elif output['variability'] == 'parameter':
                record_variable = True
                variable_df.loc[index_counter, 'type'] = 'parameter'
            elif complete_set and record_variable == False:
                record_variable = True
                variable_df.loc[index_counter, 'type'] = 'internal'
            else:
                pass
            if record_variable:
                for column in variable_df.columns:
                    if column in output.keys():
                        variable_df.loc[index_counter, column] = output[column]
                index_counter += 1

        return variable_df

    def generate_code_analysis_inputs_1(self, modelica_package_tree_path):
        '''Generate inputs for code analysis by extracting relevant information from the Modelica model.'''

        variable_df = self.parse_model_variables(modelica_package_tree_path, True)
        # connections_list = self.omc.sendExpression(f'getConnectionList({modelica_package_tree_path})')

        # Read the Modelica file and extract equation sections and algorithm sections
        filepath = os.path.join(self.lib_root, *modelica_package_tree_path.split('.')) + '.mo'
        with open(filepath, 'r', encoding='utf-8') as f:
            model_code = f.read()
        sections = re.findall(
            r'(?sm)'
            r'(^[ \t]*(?:equation|algorithm)\b.*?)'
            r'(?=^[ \t]*(?:equation|algorithm|end[ \t]+(?!if\b|for\b|when\b|while\b))\b)',
            model_code
        )
        connections_list = '\n'.join(sections)
        connections_list = strip_annotations(connections_list)

        return variable_df, connections_list

    def generate_code_analysis_inputs_2(self, modelica_package_tree_path):
        '''Analyze the Modelica code based on the extracted variables and connections and generate code documentation.'''
        variable_df, connections_list = self.generate_code_analysis_inputs_1(modelica_package_tree_path)
        internal_context_df = pd.DataFrame(columns=['className', 'connectorsDf', 'classComment'])

        # Additional context for internal variables
        internal_variables_classes = variable_df[variable_df['type'] == 'internal']['className'].tolist()
        for index, class_name in enumerate(internal_variables_classes):
            class_comment = self.omc.sendExpression(f'getClassComment({class_name})')
            internal_connectors_df = self.parse_model_variables(class_name)
            internal_connectors_df = internal_connectors_df[internal_connectors_df['className'].apply(lambda x: 'interfaces' in x.lower())]
            internal_context_df.loc[index, 'className'] = class_name
            internal_context_df.loc[index, 'connectorsDf'] = internal_connectors_df.to_json(orient='records')
            internal_context_df.loc[index, 'classComment'] = class_comment

        variable_md = variable_df.to_markdown(index=False)
        internal_context_md = internal_context_df.to_markdown(index=False)

        return variable_md, connections_list, internal_context_md

    def generate_english_documentation(self, modelica_package_tree_path):
        '''Generate English documentation for the Modelica model based on the extracted variables
        and connections.'''
        variable_md, connections_list, internal_context_md = self.generate_code_analysis_inputs_2(modelica_package_tree_path)
        documentation_message = f"Based on the following information about a Modelica model,\
            generate English documentation that describes the purpose and functionality of the\
            model. The documentation should be clear and concise, and should provide an overview\
            of the model's components, their relationships, and how they work together to achieve\
            the model's objectives. Please add HTML markups and ensure the output complies with the\
            rules:\n{self.doc_rules_contents[0]}\n\nVariables:\n{variable_md}\n\nConnections:\n{connections_list}\n\nInternal Context:\n{internal_context_md}"
        result = self.llm.invoke(documentation_message)
        return result

    def check_english_documentation(self, modelica_package_tree_path):
        '''Check the English documentation for the Modelica model based on the provided rules.'''
        variable_md, connections_list, internal_context_md = self.generate_code_analysis_inputs_2(modelica_package_tree_path)

        # Retrieve documentation for the model
        filepath = os.path.join(self.lib_root, *modelica_package_tree_path.split('.')) + '.mo'
        with open(filepath, 'r', encoding='utf-8') as f:
            modelica_text = f.read()
        documentation = regex.findall(r'annotation\s*(\((?:[^()]|(?1))*\))\s*;\s*end\s+\w+\s*;', modelica_text)

        check_message = f"Based on the following rules, check the English documentation in the\
            prompt for clarity, conciseness, and compliance with the provided\
            guidelines. Please provide feedback in a markdown file on any areas that could be improved and suggest\
            specific changes to enhance the quality of the documentation. The output should consist\
            of three sections: the first consists of mandatory edit suggestions because certain\
            documentation rules are being broken. The second should provide suggested edits because\
            information may be missing from the documentation. The third should provide general\
            comments and recommendations for improvement.\
            The feedback should be a concise and clear list with each item having 3 columns for\
            the original text with issue, the suggested edit, and the rationale.\
            Ensure you add '`' signs\
            around any HTML code referenced in the output so that it doesn't break the formatting\
            of the md output.The variables, connections and context give you more details about the model.\
            Here are the rules:\n{self.doc_rules_contents[0]}\n\nDocumentation:\n{documentation}.\n\nVariables:\n{variable_md}\n\nConnections:\n{connections_list}\n\nInternal Context:\n{internal_context_md}"
        result = self.llm.invoke(check_message)
        print(result)
        return result

    def get_pseudo_code(self, modelica_package_tree_path):
        '''Generate pseudo-code for the Modelica model based on the extracted variables and connections.'''
        variable_md, connections_list, internal_context_md = self.generate_code_analysis_inputs_2(modelica_package_tree_path)
        pseudocode_message = f"Based on the following information about a Modelica model,\
            generate pseudo-code that describes the logic and flow of the\
            model. The pseudo-code should be clear and concise, and should provide an overview\
            of the model's components, their relationships, and how they work together to achieve\
            the model's objectives. Please output the pseudocode as a markdown file.\
            \n\nVariables:\n{variable_md}\n\nConnections:\n{connections_list}\n\nInternal component Context:\n{internal_context_md}"
        result = self.llm.invoke(pseudocode_message)
        return result

if __name__ == "__main__":
    API_KEY = "" # Your API key for Claude Depot
    BASE_URL = "" # Base URL for the API
    # MODEL = 'claude-sonnet-4-6-birthright'
    MODEL = 'grok-4-fast-reasoning-birthright'

    lib_build = os.path.abspath(os.path.join('..', '..', 'buildings_library', 'modelica-buildings', 'Buildings'))
    example_path = os.path.normpath(os.path.join(lib_build, 'Controls', 'OBC', 'CDL', 'Examples'))
    cdl_root = os.path.abspath(os.path.join(example_path, '..'))
    lib_root_trial = os.path.normpath(os.path.join(lib_build, '..'))
    output_dir = os.path.abspath('.')
    os.environ['MODELICAPATH'] = os.path.dirname(lib_root_trial)

    checker = ModuleCheck(MODEL, BASE_URL, API_KEY, lib_root_trial, True)
    # TEST_FILE = 'Buildings.Templates.Plants.Controls.HeatPumps.AirToWater'
    TEST_FILE = 'Buildings.Templates.Plants.Controls.StagingRotation.EquipmentEnable'
    english_docs = checker.generate_english_documentation(TEST_FILE)
    output_file_path = os.path.join(output_dir, 'DocumentationGeneration_042226', f'sonnet46_{TEST_FILE.split(".")[-1]}.html')
    if not os.path.exists(os.path.dirname(output_file_path)):
        os.makedirs(os.path.dirname(output_file_path))
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(english_docs)
    # print(english_docs)
    # # analysis_result = checker.analyze_variable_names(variables)
    # # print(analysis_result)

    # checker_2 = ModuleCheck(MODEL, BASE_URL, API_KEY, lib_root_trial, True)
    # pseudocode = checker_2.get_pseudo_code(TEST_FILE)
    # print(pseudocode)

    # # Write analysis result to a markdown file
    # with open(os.path.join(output_dir, 'english_documentation.html'), 'w', encoding='utf-8') as f:
    #     f.write(english_docs)

    # with open(os.path.join(output_dir, 'pseudocode.md'), 'w', encoding='utf-8') as f:
    #     f.write(pseudocode)

    # reqd_class = ['Buildings.Templates.Plants.Controls.HeatPumps.AirToWater',
    #               'Buildings.Templates.Plants.Controls.StagingRotation.EventSequencing',
    #               'Buildings.Templates.Plants.Controls.StagingRotation.EquipmentEnable',
    #               'Buildings.Templates.Plants.Controls.StagingRotation.StageChangeCommand',
    #               'Buildings.Templates.Plants.Controls.StagingRotation.HybridOperation']

    # for class_path in reqd_class:
    checker_3 = ModuleCheck(MODEL, BASE_URL, API_KEY, lib_root_trial, True)
    feedback = checker_3.check_english_documentation(TEST_FILE)
    with open(os.path.join(output_dir, 'DocumentationFeedback_042226', f'sonnet46_{TEST_FILE.split(".")[-1]}_2.md'), 'w', encoding='utf-8') as f:
        f.write(feedback)
