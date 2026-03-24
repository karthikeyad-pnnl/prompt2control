from typing import Any, List, Optional
from langchain.llms.base import LLM
import requests
import os
import openai
#get key as needed
#key = os.getenv("API_KEY", "your_default_api_key_here")

class ClaudeDepotLLM():
    """Base wrapper for Claude models served."""
#set model, url api as needed
    def __init__(self, model: str = "text-embedding-3-small-birthright", base_url: str = "your based url", api_key: Optional[str] = 'key', system_message: Optional[str] = None):

        self.model = model
        self.base_url = base_url
        self.api_key = api_key
        self.system_message = system_message if system_message is not None else "You are a code generator. Only return valid Modelica code with no natural language, no explanations, and no comments."

    def invoke(self, prompt: str, stop: Optional[List[str]] = None):
        client = openai.OpenAI(api_key=self.api_key, base_url=self.base_url)

        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": prompt}
            ]
        )

        # data = response.model_dump_json()
        return response.choices[0].message.content

    @property
    def _llm_type(self) -> str:
        return "claude-depot"

# Example usage
if __name__ == "__main__":
    llm = ClaudeDepotLLM()
    prompt = (
        "My friend says lights are dark sinks, not sources. "
        "Explain how to prove they're wrong using physics."
    )
    result = llm.invoke(prompt)
    print(result)
