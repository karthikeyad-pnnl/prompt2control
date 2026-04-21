import os
from claude import ClaudeDepotLLM
from search import gather_cdl_modules
from ModuleGenerator import ModuleGenerator
from ModuleEvaluate import ModelicaModuleComparator

##User Input
API_KEY = "" # Your API key for Claude Depot
BASE_URL = "" # Base URL for the API
FOLDER_PATH = "CDL"
# MODEL = 'claude-sonnet-4-6-birthright'
MODEL = 'text-embedding-3-small-birthright'

def main():

    # Initialize the generator with the dummy LLM and specify paths.
    SYSTEM_MESSAGE_1 = """
            You are a code generator. Only return valid Modelica code with no natural language, no explanations, and no comments.

            Follow these additional modeling and layout conventions:

            - Use only modules from Buildings.Controls.OBC.CDL.
            - For any temperature-related `input` or `parameter`, use:
            `final unit="K", displayUnit="degC", final quantity="ThermodynamicTemperature"`.
            - For normalized output signals (e.g., y = 0 or 1), use: 
            `final min=0, final max=1, final unit="1"`.

            Graphic layout guidance:
            - Use the order of `connect()` statements in the `equation` section to infer logic flow: upstream instances appear earlier as sources, downstream ones appear later as targets.
            - Reflect this left-to-right logic flow in the respective `annotation` statements for each block instance by placing upstream components to the left and downstream components to the right.
            - Ensure all instances are positioned with unique `(x, y)` coordinates to avoid overlapping.
            - Use clear spacing between instances to improve readability in the `diagram` layer.
            - Annotate instances with their names where appropriate to enhance visual understanding.
            """

    SYSTEM_MESSAGE_2 = "You are an expert Building Control engineer. Respond in structured, clear text."
    SYSTEM_MESSAGE_3 = "You are an expert to evaluate Modelica models. You can only answer yes or no."

    ##User Input
    #change model name as needed
    llm_1 = ClaudeDepotLLM(model=MODEL, api_key=API_KEY, system_message=SYSTEM_MESSAGE_1, base_url=BASE_URL)
    llm_2 = ClaudeDepotLLM(model=MODEL, api_key=API_KEY, system_message=SYSTEM_MESSAGE_2, base_url=BASE_URL)
    llm_3 = ClaudeDepotLLM(model=MODEL, api_key=API_KEY, system_message=SYSTEM_MESSAGE_3, base_url=BASE_URL)

    lib_build = os.path.abspath(os.path.join('..', '..', 'buildings_library', 'modelica-buildings', 'Buildings'))
    example_path = os.path.normpath(os.path.join(lib_build, 'Controls', 'OBC', 'CDL', 'Examples'))
    cdl_root = os.path.abspath(os.path.join(example_path, '..'))
    lib_root = os.path.normpath(os.path.join(lib_build, '..'))
    output_dir = os.path.abspath('.')
    os.environ['MODELICAPATH'] = os.path.dirname(lib_root)


    evaluate = ModelicaModuleComparator()
    quest_file = os.path.abspath("./test.json")
    quest = evaluate.load_json_metadata(quest_file) # Test Cases
    generator = ModuleGenerator(
            llm1=llm_1,
            llm2=llm_2,
            llm3=llm_3,
            base_library_paths=[lib_build],              # Load the Modelica Standard Library
            output_dir=output_dir,                               # Save files to current directory
            library_dir=example_path,   # Path to target library (e.g., an Examples package in a library)
            cdl_list= "cdl_models_prompt.txt", # availalbe modules in CDL
            cdl_root=cdl_root,
            lib_root = lib_root
        )

    generator.setup_openmodelica()
    for item in quest:
        generator.keep_only_package_mo()
        key = item['id']
        title = "Task" + key
        prompt_text=item['prompt']
        generator.title = title
        generator.prompt_text = prompt_text
        _ = generator.identify_modules()
        _ = generator.generate_code_iterate()
        _ = generator.save_modelica_file()
        generator.copy_to_library()
        generator.check_and_fix_model()
        generator.simulate_and_fix_model()

if __name__ == "__main__":
    main()
