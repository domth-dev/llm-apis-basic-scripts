import os
from mistralai import Mistral
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["MISTRAL_API_KEY"]
model = "ministral-3b-2410"

client = Mistral(api_key=api_key)

messages = []

message_system = { "role": "system", "content": "You are a helpfull assistant."}
message_user = { "role": "user", "content": "Hello, how can you assist me today?"}

messages.append(message_system)
messages.append(message_user)

response = client.chat.complete(
    model = model,
    messages = messages
)

print(response.choices[0].message.content)
print(response)