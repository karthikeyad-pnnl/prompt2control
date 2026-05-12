from typing import List, Optional
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
        self.client = openai.OpenAI(api_key=self.api_key, base_url=self.base_url)
        self.messages = [
            {"role": "system", "content": self.system_message}
        ]

    def invoke(self, prompt: str, stop: Optional[List[str]] = None):

        self.messages.append({"role": "user", "content": prompt})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )

        response_message = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": response_message})

        return response_message

    @property
    def _llm_type(self) -> str:
        return "claude-depot"

# Example usage
if __name__ == "__main__":
    ##User Input
    API_KEY = "" # Your API key for Claude Depot
    BASE_URL = "" # Base URL for the API
    MODEL = "grok-4-fast-reasoning-birthright"
    llm = ClaudeDepotLLM(api_key=API_KEY, base_url=BASE_URL, model=MODEL, system_message='You are a linguist.')
    # llm = openai.OpenAI(api_key=API_KEY, base_url=BASE_URL)

    PROMPT_1 = '''Reverse the letters in the next prompt.'''
    result = llm.invoke(PROMPT_1)
    print("\n\nModel response-1:")
    print(result)
    result = llm.invoke("What is the question?")
    # result = llm.chat.completions.create(
    #     model=MODEL,
    #     messages=[
    #         {"role": "user", "content": PROMPT_1}
    #     ]
    # )
    print("\n\nModel response-2:")
    print(result)
    # print(result.choices[0].message.content)
