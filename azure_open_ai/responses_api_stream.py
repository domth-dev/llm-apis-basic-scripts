import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

instructions = "You are a helpful assistant."
user_input = "What is the capital of France?"

stream_response = client.responses.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    instructions=instructions,
    input=user_input,
    stream=True
)

for chunk in stream_response:
    if chunk.type == 'response.output_text.delta':
        content = chunk.delta
        print(content, end='', flush=True)