
from groq import Groq
from dotenv import load_dotenv
from pydantic import BaseModel
from pathlib import Path
import os
import json

# Load environment variables from project root
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

model = "openai/gpt-oss-20b"


# Define the structure using Pydantic
class Ticket(BaseModel):
    name: str
    email: str
    issue: str


# Generate JSON schema
schema = Ticket.model_json_schema()

response_format = {
    "type": "json_object"
}


# System prompt
system_prompt = f"""
Extract information from the customer ticket.

Return valid JSON strictly following this schema:
{json.dumps(schema)}

Do not invent information.
"""


message_system = {
    "role": "system",
    "content": system_prompt
}


# Customer ticket
text = """
Hello, my name is Dharamveer. I have an iPhone which is not
working properly. I want to get it repaired.

My address is 1234, Main Street, New York.
My email is dharamveer@example.com.
My father's name is ABC and contact number is 1234567890.
My mother's name is XYZ and contact number is 0987654321.
My date of birth is 01/01/1990.
"""


# User prompt
prompt = f"""
Extract the customer's name, email, and issue.

Customer ticket:
{text}
"""


message_user = {
    "role": "user",
    "content": prompt
}


# Send request to Groq
response = client.chat.completions.create(
    model=model,
    messages=[message_system, message_user],
    response_format=response_format,
    temperature=0
)


# Get the AI response
answer = response.choices[0].message.content




# Convert JSON string into a Python dictionary
raw_json = answer
data_file = json.loads(raw_json)


# Validate data using Pydantic
ticket = Ticket(**data_file)

print("\nValidated ticket:")
print(ticket)

print("\nName:", ticket.name)
print("Email:", ticket.email)
print("Issue:", ticket.issue)

# homework

# take reume in pdf or word
# have hr give a list of thind like skills experiunebce ,projects
# extract these fromm resume
# match agiansthr listgenerate a percaentage matching or not
