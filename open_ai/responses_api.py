from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

instructions = "You are a helpful assistant."
user_input = "What is the capital of France?"

response = client.responses.create(
    model="gpt-4o",
    instructions=instructions,
    input=user_input,
    stream=True
)

print(response.output_text)
#print(response.output[0].content[0].text)