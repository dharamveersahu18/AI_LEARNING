
# RCOEF follows for prompt
# R -> Role , C-> Constraint , O -> Output Format, E ->Example, f-> Fallback
import os
from dotenv import load_dotenv
from groq import Groq

# 1. Load variables from .env
load_dotenv()

# 2. Get API key
my_api_key = os.getenv("GROQ_API_KEY")

# 3. Create Groq client
client = Groq(api_key=my_api_key)

# 4. Select model
model = "openai/gpt-oss-20b"


# 5. Function to get an answer from the LLM
def llm_ans(prompt):
    message = {
        "role": "user",
        "content": prompt
    }

    messages = [message]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    answer = response.choices[0].message.content
    return answer


# 6. Give the LLM a complaint to classify
bad_prompt = """
#Role
You area a support assistant at a mobile /laptop comapnay
#Task:
you  have to classify the issue in a category
#Constraint:
you have to classify the issue in one of the namely billing ,technical return
This is a user complaint:
#Example
for instance if  a user complaints sys hw want  a refund then category return

#Fallback
if the issue is unrealted to any of the categories mentioned in constraints,than the nasweer should be OTHER
#output
format
your answer should be in one word only. the one word should be one of the categories given in constriants
my marraige is broken
"""

print(llm_ans(bad_prompt))
