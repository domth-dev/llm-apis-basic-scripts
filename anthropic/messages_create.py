import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

messages = []

message_system = [{ "type": "text", "text": "You are a helpfull assistant."}]
message_assistant = { "role": "assistant", "content": "Hello."}
message_user = { "role": "user", "content": "Hello, how can you assist me today?"}

messages.append(message_assistant)
messages.append(message_user)

response = client.messages.create(
    model="claude-3-5-haiku-latest",
    max_tokens=1000,
    messages=messages,
    system=message_system
)

print(response.content)