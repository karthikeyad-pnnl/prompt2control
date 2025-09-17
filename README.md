# Prompt2Control

This project converts high-level control task descriptions into valid Modelica modules using a LangChain-driven prompt-engineering pipeline, OpenModelica backend, and LLM integration.

---

## 📁 Project Structure

- `main.py` – Entry point of the application.
- `claude.py` – Custom wrapper for Claude LLM (ClaudeDepotLLM).
- `search.py` – Gathers CDL module definitions from local libraries.
- `cdl_models_prompt.txt` – Stores extracted CDL module content.
- `ModuleGenerator.py` – Contains class to iteratively generate Modelica modules from control prompts.
- `ModuleEvaluate.py` – Evaluates generated Modelica modules using LLM reasoning.
- `modelica_post_process.py` – Applies rule-based filters to clean/refactor Modelica code.
- `test.py` – Contains test examples for running full generation-evaluation cycles.
- `convert.py` - Convert .mat simulation results into .txt format.

---

## 🚀 Features

- LangChain-based prompt orchestration
- Support for different LLMs
- Integration with OpenModelica via `OMPython`
- Automatic module generation, evaluation, and formatting
- Local CDL module search and context embedding

---

## 🛠️ Installation

1. **Clone the repository**

```bash
git clone https://tanuki.pnnl.gov/GenAI/thrust-two-pilot-projects/prompt2control.git
cd prompt2control
````

2. **Set up Python environment**

```bash
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. **Install OpenModelica**

Download and install OpenModelica from: [https://openmodelica.org/](https://openmodelica.org/)

Ensure `OMCSessionZMQ` is operational:

```bash
python -c "from OMPython import OMCSessionZMQ; omc = OMCSessionZMQ(); print(omc.sendExpression('getVersion()'))"
```

4. **Download Buildings Library**

Clone the Modelica Buildings library:

```bash
git clone https://github.com/lbl-srg/modelica-buildings.git
```
Make sure to point your model or simulation environment to this library directory when loading or compiling models.

---

## 📦 Usage

```bash
python main.py
```

This will:

1. Load CDL module context.
2. Prompt Claude with a control task.
3. Generate Modelica code.
4. Evaluate and refine it using post-processing and LLM-based review.

You can modify test cases in `test.py` or system prompts in `main.py`

---

## 🧱 Dependencies

See [`requirements.txt`](requirements.txt)

---

## 🔒 Notes

* Claude LLM is expected to be used and has the best performance.
* CDL modules must be indexed locally via `search.py` into `cdl_models_prompt.txt`.

---

## 🙏 Acknowledgments

The research described herein was funded by the *Generative AI for Science, Energy, and Security* Science & Technology Investment under the Laboratory Directed Research and Development Program at PNNL, a multiprogram national laboratory operated by Battelle for the U.S. Department of Energy.  

This work was also supported by the Center for AI and the Center for Continuum Computing at PNNL.