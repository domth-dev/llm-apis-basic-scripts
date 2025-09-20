import os
from typing import List, Dict, Any, Iterator
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class GoogleGeminiProvider:
    def __init__(self, system_message: str) -> None:
        self.model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        self.system_message = system_message

    def response(self, messages: List[Dict[str, Any]]) -> Iterator[str]:
        joined = " ".join(str(m.get("content", "")) for m in messages)
        stream = client.models.generate_content_stream(
            model=self.model,
            config=types.GenerateContentConfig(system_instruction=self.system_message),
            contents=joined,
        )
        for chunk in stream:
            content = getattr(chunk, "text", None)
            if content:
                yield content
