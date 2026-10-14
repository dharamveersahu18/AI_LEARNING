
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# System role: Define the AI's personality and behavior

message_system = {
    "role": "system",
    "content": (
        "You are a strict office colleaguej who is my manager. "    
    )
}

message = {
    "role": "user",
    "content": " ilove you baby."
}

# Send messages to the AI
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[message_system, message],
    temperature=1
)

# Print the AI's response
answer = response.choices[0].message.content

print(f"Answer: {answer}")