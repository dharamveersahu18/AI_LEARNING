
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Define 3 prompts
prompt1 = "Hi!"
prompt2 = "Explain the current job market situation for BSc CS students in India."
prompt3 = "Write 100 words about biodiversity."

prompts = [prompt1, prompt2, prompt3]

# System role: Define AI's behavior
role = "You are a helpful AI assistant. Give clear and simple answers."

for prompt in prompts:

    # System message: Instructions for the AI
    message_system = {
        "role": "system",
        "content": role
    }

    # User message: Actual question
    message = {
        "role": "user",
        "content": prompt
    }

    # Send messages to the AI
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[message_system, message],
        temperature=1,
        max_tokens=100,

    )
    usage= response.usage
    print(f"Prompt: {prompt}  --> token completion_token : {usage.completion_tokens} , prompt_token : {usage.prompt_tokens} , total_token : {usage.total_tokens} Finish Reason: {response.choices[0].finish_reason}")

    # Extract and print the AI's response
    answer = response.choices[0].message.content

    print(f"\nQuestion: {prompt}")

    print("-" * 50)