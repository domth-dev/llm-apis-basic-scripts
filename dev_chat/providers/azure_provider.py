import os
from typing import List, Dict, Any, Iterator
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

class AzureProvider:
    def __init__(self, system_message: str) -> None:
        self.model = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
        self.system_message = system_message

    def response(self, messages: List[Dict[str, Any]]) -> Iterator[str]:
        full = []
        if self.system_message:
            full.append({"role": "system", "content": self.system_message})
        full.extend(messages)
        stream = client.chat.completions.create(
            model=self.model,
            messages=full,
            stream=True,
        )
        for chunk in stream:
            if chunk and hasattr(chunk, "choices") and len(chunk.choices) > 0:
                delta = chunk.choices[0].delta
                content = getattr(delta, "content", None)
                if content:
                    yield content
