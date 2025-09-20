import os
from typing import List, Dict, Any, Iterator
from mistralai import Mistral
from dotenv import load_dotenv

load_dotenv()

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])  # raises if missing

class MistralProvider:
    def __init__(self, system_message: str) -> None:
        self.model = os.getenv("MISTRAL_MODEL", "ministral-3b-2410")
        self.system_message = system_message

    def response(self, messages: List[Dict[str, Any]]) -> Iterator[str]:
        full = []
        if self.system_message:
            full.append({"role": "system", "content": self.system_message})
        full.extend(messages)
        stream = client.chat.stream(model=self.model, messages=full)
        for chunk in stream:
            content = chunk.data.choices[0].delta.content
            if content is not None:
                yield content
