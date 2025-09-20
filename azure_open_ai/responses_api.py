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

response = client.responses.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    instructions=instructions,
    input=user_input
)

print(response.model_dump_json(indent=2))
#print(response.output[0].content[0].text)