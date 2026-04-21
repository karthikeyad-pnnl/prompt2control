import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from search import gather_cdl_modules
from modelica_post_process import clean_modelica_code
from OMPython import OMCSessionZMQ
import shutil
import DyMat as dymat
from convert import MatToTextExporter

def load_simulation_variables(mat_file_path, variable_names=None, max_samples=100):
    """
    Load selected variables from a Modelica .mat result file.
    """
    reader = dymat.DymolaMatReader(mat_file_path)
    result = {}
    time = reader['Time']
    result['Time'] = time[:max_samples].tolist()

    if variable_names is None:
        variable_names = [k for k in reader.names if not k.startswith('der(')]

    for var in variable_names:
        if var in reader:
            result[var] = reader[var][:max_samples].tolist()
    return result

class ModuleGenerator:
    """
    A class to generate and validate Modelica control modules using a language model and OpenModelica.
    Encapsulates functionality for code generation, file handling, and OpenModelica compilation.
    """
    def __init__(self, llm1,llm2,llm3, base_library_paths=None, output_dir=".", library_dir=".", cdl_list="cdl_models_prompt.txt", cdl_root=".",lib_root = '.', prompt_text=None, title=None):
        """
        Initialize the generator with external dependencies and paths.
        :param llm: An instance of a language model (with a `generate(prompt)` method) for code generation and fixes.
        :param base_library_paths: List of Modelica libraries (names or file paths) to load for context (e.g., ["Modelica", "/path/to/Buildings.mo"]).
        :param output_dir: Directory where generated Modelica files will be saved initially.
        :param library_dir: Directory of the Modelica package where new models should be copied for integration.
        """
        self.llm1 = llm1 #code generation
        self.llm2 = llm2 #code improvement
        self.llm3 = llm3 #code evaluate yes/no
        self.base_library_paths = base_library_paths if base_library_paths else []
        self.output_dir = os.path.abspath(output_dir)
        self.library_dir = os.path.abspath(library_dir)
        self.cdl_list = os.path.abspath(cdl_list)
        self.cdl_root = os.path.abspath(cdl_root)
        self.prompt_text = prompt_text
        self.title = title
        self.omc = None  # Will hold the OpenModelica OMC session after setup.
        self.lib_root = os.path.abspath(lib_root)

    def load_available_modules(self, file_path):
        """
        Load available CDL modules from a text file.
        The file is expected to contain module definitions or listings. 
        Returns a dictionary mapping module names to their code (or description).
        """
        file_path = os.path.abspath(file_path)
        with open(file_path, "r", encoding="utf-8") as f:
            available_modules = f.read()
        return available_modules

    def identify_modules(self, prompt_text=None, title = None):
        """
        Use the language model to identify the minimal set of module names required for the given control task.
        :param prompt_text: Description of the control task or problem.
        :return: List of module names (strings) that are needed for the task.
        """
        if prompt_text is None:
            prompt_text = self.prompt_text
        if title is None:
            title = self.title
        available_modules = self.load_available_modules(self.cdl_list)
        # === STEP 1: CDL module listing ===
        basic_logic_prompt = ChatPromptTemplate.from_template("""
                            Given the following control task, and available CDL module name, list the **CDL modules** you would use in bullet 
                            points with no explanations, no comments. As few as possible CDL modules should be used to achieve the task.
                            Return only a list of the module names as Python list of items, with each item representing a module, but
                            without the square brackets for the list.

                            Task:
                            {task}

                            available CDL modules:
                            {txt}
                            """)
        step1_prompt = basic_logic_prompt.format(task=prompt_text, txt=available_modules)
        # print("Prompt for module identification:\n", step1_prompt)
        step1_result = self.llm2.invoke(step1_prompt)
        step1_result_clean = StrOutputParser().invoke(step1_result)
        module_list = [line.replace("•", "").replace("-", "").strip()
                   for line in step1_result_clean.strip().splitlines() if line.strip()]
        gathered_modules = gather_cdl_modules(module_list, cdl_root=self.cdl_root)
        modules_context = "\n\n".join(gathered_modules)
        self.module_list = module_list
        self.modules_context = modules_context
        return module_list

    def generate_code(self, prompt_text=None, modules_context=None):
        """
        Use the language model to generate Modelica code for the control task, given the relevant module names.
        Gathers the definitions of the selected modules as context for the LLM.
        :param prompt_text: Description of the control task.
        :param module_names: List of module names (from available_modules) to use in the code.
        :return: A string containing the generated Modelica code.
        """
        if prompt_text is None:
            prompt_text = self.prompt_text
        if modules_context is None:
            modules_context = self.modules_context
        prompt1 = ChatPromptTemplate.from_template("""
                            Using these relevant CDL modules:
                            {modules}

                            and the control task:
                            {task}

                            Generate the Modelica code block that fulfills the control task.
                            """)
        step1 = (prompt1 | self.llm1)
        final_result = step1.invoke({
            "modules": modules_context,
            "task": prompt_text
        })
        final_result_clean = StrOutputParser().invoke(final_result)
        lines = final_result_clean.strip().splitlines()
        safe_title = self.title
        lines = clean_modelica_code(lines, title=safe_title)
        final_cleaned_code = "\n".join(lines)
        self.final_code = final_cleaned_code
        return final_cleaned_code

    def save_modelica_file(self, code=None, title=None):
        """
        Save the generated Modelica code to a .mo file.
        :param code: The Modelica code as a string.
        :param title: A title for the model (used for filename and class name).
        :return: The file path of the saved .mo file.
        """
        if code is None:
            code = self.final_code
        if title is None:
            title = self.title
        mo_path = os.path.join(self.output_dir, f"{title}.mo")
        with open(mo_path, "w", encoding="utf-8") as f:
            f.write(code)
        return mo_path

    def copy_to_library(self, mo_path=None):
        """
        Copy the .mo file to the Modelica library directory and update package.order.
        This allows the new model to be recognized as part of the library/package.
        :param mo_path: Path to the .mo file to copy.
        :param safe_title: Name of the model (same as the class name, typically).
        :return: Path of the copied file within the library directory.
        """
        if mo_path is None:
            mo_path = os.path.join(self.output_dir, f"{self.title}.mo")
        safe_title = self.title
        dest_dir = self.library_dir
        os.makedirs(dest_dir, exist_ok=True)
        # Copy file into the library directory (e.g., Examples package)
        dest_path = os.path.join(dest_dir, safe_title + ".mo")
        shutil.copy(mo_path, dest_path)
        # Update or create package.order to include the new model
        order_file = os.path.join(dest_dir, "package.order")
        if os.path.exists(order_file):
            # Append the model name if not already listed
            with open(order_file, 'r+', encoding='utf-8') as f:
                lines = [line.strip() for line in f.readlines() if line.strip()]
                if safe_title not in lines:
                    lines.append(safe_title)
                    f.seek(0)
                    f.write("\n".join(lines) + "\n")
        else:
            # No package.order exists, create one with this model
            with open(order_file, 'w', encoding='utf-8') as f:
                f.write(safe_title + "\n")
        return dest_path

    def setup_openmodelica(self):
        """
        Initialize an OpenModelica OMC session and load base libraries.
        Must be called before compiling or simulating models.
        """
        # Start a new OMC session
        self.omc = OMCSessionZMQ()

        # Load standard Modelica library
        error_modelica = self.omc.sendExpression('loadModel(Modelica)')
        success_modelica = 'error' not in str(error_modelica).lower()
        print("✅ Success loading Modelica:", success_modelica)
        print("📄 Modelica load message:\n", error_modelica)

        # Load Buildings library
        buildings_package = os.path.join(self.lib_root, "Buildings", "package.mo")
        error_buildings = self.omc.sendExpression(f'loadFile("{buildings_package.replace("'",'').replace('\\','/')}")') # Path seperators are replaced since OMC expects UNIX style paths
        success_buildings = 'error' not in str(error_buildings).lower()
        print("✅ Success loading Buildings:", success_buildings)
        if not success_buildings:
            raise RuntimeError(f"Failed to load Buildings library at {buildings_package}. Check the OMC error message for details: {error_buildings}")
        print("📄 Buildings load message:\n", error_buildings)

    def check_and_fix_model(self, filepath=None, max_attempts=3):
        """
        Compile the Modelica model file with OpenModelica, and attempt to fix syntax errors if they occur.
        Uses the LLM to suggest fixes based on compiler error messages.
        :param filepath: Path to the .mo file to compile.
        :param max_attempts: Maximum number of fix attempts if errors persist.
        :return: True if the model compiled successfully (possibly after fixes), False if not.
        """
        localpath = os.path.abspath(os.path.join(self.output_dir, f"{self.title}.mo"))
        if filepath is None:
            filepath = localpath
        else:
            filepath = os.path.abspath(filepath)
        if self.omc is None:
            raise RuntimeError("OMC session not initialized. Call setup_openmodelica() first.")
        for attempt in range(1, max_attempts+1):
            # Try loading/compiling the Modelica file
            try:
                self.omc.sendExpression(f'loadFile("{filepath.replace("'",'').replace('\\','/')}")')
                error_log = ''
            except Exception as e:
                error_log = e
            if not error_log or "error" not in str(error_log).lower():
                # No compile errors (success)
                print(f"Model compiled successfully on attempt {attempt}.")
                return True
            # If error encountered, use LLM to attempt a fix
            print(f"Attempt {attempt}: Compilation error detected, using LLM to suggest a fix.")
            with open(filepath, 'r', encoding='utf-8') as f:
                code_content = f.read()
            fix_prompt = (
                "The following Modelica code has compilation errors:\n"
                f"{error_log}\n"
                "Please suggest a corrected version of the code.\n"
                "Code:\n" + code_content + "\n\n"
                "Corrected Modelica code:"
            )
            fix_response = self.llm1.invoke(fix_prompt)
            fixed_code = str(fix_response) if not isinstance(fix_response, str) else fix_response
            lines = fixed_code.strip().splitlines()
            safe_title = self.title
            lines = clean_modelica_code(lines, title=safe_title)
            final_cleaned_code = "\n".join(lines)
            # Overwrite the file with the fixed code for the next iteration
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(final_cleaned_code)
            with open(localpath, 'w', encoding='utf-8') as f:
                f.write(final_cleaned_code)
            # (Loop will retry compilation with the new code in the next iteration)
        # If all attempts fail, return False
        return False


    def simulate_and_fix_model(self, filepath=None, max_attempts=5, startTime=0, stopTime=1200):
        if filepath is None:
            filepath = os.path.abspath(os.path.join(self.library_dir, f"{self.title}.mo"))
        else:
            filepath = os.path.abspath(filepath)
        localpath = os.path.abspath(os.path.join(self.output_dir, f"{self.title}.mo"))
        prompt_text = self.prompt_text
        model_name = os.path.splitext(os.path.basename(filepath))[0]
        full_model_class = f"Buildings.Controls.OBC.CDL.Examples.{model_name}"

        for attempt in range(1, max_attempts + 1):
            print(f"Attempt {attempt}: Loading and simulating model ...")

            # Load package
            model_path = os.path.normpath(os.path.join(self.lib_root, "Buildings", "Controls", "OBC", "CDL", "Examples", f"{model_name}.mo"))
            try:
                self.omc.sendExpression(f'loadFile("{model_path.replace("'",'').replace('\\','/')}")')
                error_msg = ''
            except Exception as e:
                error_msg = str(e)

            if "error" in error_msg.lower():
                print("Cannot load file; Error: ", error_msg)
                return False

            # Simulate
            cmd = f'simulate({full_model_class}, startTime={startTime}, stopTime={stopTime})'
            try:
                result = self.omc.sendExpression(cmd)
                print("Simulation result:", result)
            except Exception as e:
                error_msg = str(e)

            if "error" in error_msg.lower():
                print(f"Simulation error on attempt {attempt}: {error_msg}")
                with open(filepath, 'r', encoding='utf-8') as f:
                    model_code = f.read()
                prompt = ChatPromptTemplate.from_template("""
                                    Based on these relevant CDL modules:
                                    {modules}

                                    and the control task:
                                    {task}

                                    and the error message:
                                    {error}
                                    Revise the Modelica code block:
                                    {code}
                                    """)
                step1 = (prompt | self.llm1)
                final_result = step1.invoke({
                    "modules": self.modules_context,
                    "task": prompt_text,
                    "error": error_msg,
                    "code": model_code
                })
                fixed_code = str(final_result)
                cleaned = "\n".join(clean_modelica_code(fixed_code.strip().splitlines(), title=self.title))
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(cleaned)
                with open(localpath, 'w', encoding='utf-8') as f:
                    f.write(cleaned)
                continue  # retry outer loop

            # --- Check if simulation result meets control goals ---
            try:
                result_path = full_model_class + "_res.mat"
                with open(filepath, 'r', encoding='utf-8') as f:
                    model_code = f.read()
                clean_temp_files()
                output_path = full_model_class + "sim_res.txt"
                exporter = MatToTextExporter(result_path, output_path)
                exporter.export_summary()
                with open(output_path, 'r', encoding='utf-8') as f:
                    formatted_output = f.read()
            except Exception as e:
                formatted_output = f"(Could not load simulation results due to error: {e})"
                return False

            for sub_attempt in range(1, max_attempts + 1):
                print(f"Sub_Attempt {sub_attempt}: Evaluating result ...")
                llm_prompt = (
                    f"The control task is:\n{prompt_text}\n\n"
                    f"The simulation ran successfully and produced the following outputs:\n{formatted_output}\n\n"
                    "Based on this data, does the model meet the control requirements?"
                )
                validation_response = self.llm3.invoke(llm_prompt)
                print("LLM response regarding control goal:\n", validation_response)
                return True

        print("All attempts to fix and simulate the model failed.")
        return False

    def keep_only_package_mo(self, path=None):
        """
        Removes all files in the specified directory except 'package.mo'.
        """
        if path == None:
            path = self.library_dir
        if not os.path.isdir(path):
            raise ValueError(f"The specified path does not exist or is not a directory: {path}")

        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)

            # Skip directories and the 'package.mo' file
            if os.path.isfile(file_path) and filename != "package.mo":
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"Error removing {file_path}: {e}")
                    
    def generate_code_iterate(self, prompt_text=None, modules_context=None, max_rounds=3):
        if prompt_text is None:
            prompt_text = self.prompt_text
        if modules_context is None:
            modules_context = self.modules_context

        prompt1 = ChatPromptTemplate.from_template("""
            Using these relevant CDL modules:
            {modules}

            and the control task:
            {task}

            Generate the Modelica code block that fulfills the control task.
            Only use modules from Buildings.Controls.OBC.CDL or the Modelica Standard Library.
        """)

        prompt2 = ChatPromptTemplate.from_template("""
            Refer to the control task:
            {task}

            Here is the Modelica code generated in the previous step:
            {code}

            Suggest clear improvements to enhance the code's correctness or completeness in achieving the task.
            You may recommend using additional modules from the Modelica Standard Library if needed.
            Return only the improvement suggestions — no code yet.
        """)

        prompt3 = ChatPromptTemplate.from_template("""
            This is the control task:
            {task}

            Here is the original Modelica code:
            {code}

            Here are the improvement suggestions:
            {suggestion}

            Revise the original code by applying the suggestions where appropriate.
            You can use Buildings.Controls.OBC.CDL and Modelica Standard Library modules.
            Only return valid Modelica code — no natural language, no explanations, and no comments.
        """)

        evaluation_prompt = ChatPromptTemplate.from_template("""
            Given the following control task:
            {task}

            And this Modelica code:
            {code}

            Does this Modelica code fulfill the task correctly and robustly?
            Respond with either "YES" or "NO" only.
        """)

        code = None
        task = prompt_text

        for round_num in range(1, max_rounds + 1):
            if round_num == 1:
                # Generate initial code
                code = self.llm1.invoke(prompt1.format(modules=modules_context, task=task))
            else:
                # Revise based on suggestions
                suggestion = self.llm2.invoke(prompt2.format(code=code, task=task))
                code = self.llm1.invoke(prompt3.format(code=code, suggestion=suggestion, task=task))

            # Evaluate code quality
            verdict = self.llm3.invoke(evaluation_prompt.format(code=code, task=task)).strip().upper()
            if "YES" in verdict:
                break  # Exit early if model says it's good

        # Final post-processing
        code_clean = StrOutputParser().invoke(code)
        lines = code_clean.strip().splitlines()
        safe_title = self.title
        lines = clean_modelica_code(lines, title=safe_title)
        final_cleaned_code = "\n".join(lines)

        self.final_code = final_cleaned_code
        return final_cleaned_code

def clean_temp_files():
    current_dir = os.getcwd()
    deleted_files = []
    for filename in os.listdir(current_dir):
        if filename.startswith("Buildings.Controls.OBC.CDL.Examples.") and not filename.endswith(".mat"):
            try:
                full_path = os.path.join(current_dir, filename)
                os.remove(full_path)
                deleted_files.append(filename)
            except Exception as e:
                print(f"⚠️ Could not delete {filename}: {e}")
    #print(f"🧹 Deleted files: {deleted_files}")
