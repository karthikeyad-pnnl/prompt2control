from typing import Any, List, Optional
from langchain.llms.base import LLM
import requests
import os
#get key as needed
#key = os.getenv("API_KEY", "your_default_api_key_here")

class ClaudeDepotLLM(LLM):
    """Base wrapper for Claude models served."""
#set model, url api as needed
    model: str = "claude-3-7-sonnet-20250219-v1"
    base_url: str = "your based url"
    api_key: Optional[str] = key

    system_message: str = "You are a code generator. Only return valid Modelica code with no natural language, no explanations, and no comments."

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": self.system_message},
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }

        response = requests.post(self.base_url, headers=headers, json=payload)

        if response.status_code != 200:
            raise ValueError(f"Request failed: {response.status_code} - {response.text}")

        data = response.json()
        return data["choices"][0]["message"]["content"]

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
