from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

messages = []

message_system = { "role": "system", "content": "You are a helpfull assistant."}
message_user = { "role": "user", "content": "Hello, how can you assist me today?"}

messages.append(message_system)
messages.append(message_user)

stream_response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    stream=True
)

for chunk in stream_response:
  content = chunk.choices[0].delta.content
  if content is not None:
    print(content, end="", flush=True)