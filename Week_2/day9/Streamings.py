
import os
from dotenv import load_dotenv
from groq import Groq

# Load variables from .env
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai!")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-20b"
prompt = "Explain how the internet works."

messages = [
    {
        "role": "user",
        "content": prompt
    }
]

# Without streaming
response = client.chat.completions.create(
    model=model,
    messages=messages
)

answer = response.choices[0].message.content
print(answer)

# With streaming (use this instead of the block above)
# stream = client.chat.completions.create(
#     model=model,
#     messages=messages,
#     stream=True
# )

# for chunk in stream:
#     content = chunk.choices[0].delta.content
#     if content:
#         print(content, end="", flush=True)
