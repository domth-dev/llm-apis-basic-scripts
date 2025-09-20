from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

instructions = "You are a helpful assistant."
user_input = "What is the capital of France?"

stream_response = client.responses.create(
    model="gpt-4o",
    instructions=instructions,
    input=user_input,
    stream=True
)

for chunk in stream_response:
    content = chunk.text
    if content:
        print(content, end="", flush=True)