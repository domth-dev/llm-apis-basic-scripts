import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

messages = []

message_system = { "role": "system", "content": "You are a helpfull assistant."}
message_user = { "role": "user", "content": "Hello, how can you assist me today?"}

messages.append(message_system)
messages.append(message_user)

response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    messages=messages
)

print(response.choices[0].message.content)