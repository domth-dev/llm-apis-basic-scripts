import os
from typing import List, Dict, Any, Iterator
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

class AnthropicProvider:
    def __init__(self, system_message: str) -> None:
        self.model = os.getenv("ANTHROPIC_MODEL", "claude-3-5-haiku-latest")
        self.max_tokens = 1000
        self.system_message = system_message

    def response(self, messages:List[Dict[str, Any]]) -> Iterator[Any]:

        stream_response = client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=self.system_message,
            messages=messages,
            stream=True
        )

        for chunk in stream_response:
            if chunk.type == "content_block_delta":
                content = chunk.delta.text
                yield content