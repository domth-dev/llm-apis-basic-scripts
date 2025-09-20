from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

contents = "Hello, how can you assist me today?"
system_instruction = "You are a helpfull assistant."

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=system_instruction
    ),
    contents=contents
)

print(response.text)
#print(response.candidates[0].content.parts[0].text)