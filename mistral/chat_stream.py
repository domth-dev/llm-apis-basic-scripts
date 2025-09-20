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

stream_response = client.chat.stream(
    model = model,
    messages = messages
)

for chunk in stream_response:
    content = chunk.data.choices[0].delta.content
    if content is not None:
        print(content, end="", flush=True)