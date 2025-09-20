import os
from typing import List, Dict, Any, Iterator
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class OpenAIProvider:
    def __init__(self, system_message: str) -> None:
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o")
        self.system_message = system_message

    def response(self, messages: List[Dict[str, Any]]) -> Iterator[str]:
        stream = client.responses.create(
            model=self.model,
            instructions=self.system_message,
            input=messages,
            stream=True,
        )
        for chunk in stream:
            content = getattr(chunk, "text", None)
            if content:
                yield content
