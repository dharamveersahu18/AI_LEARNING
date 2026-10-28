
import os
from dotenv import load_dotenv
from groq import Groq
import time
from pathlib import Path
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-20b"

JD = """
We are hiring a Backend Python Developer.

Requirements:
- Strong Python
- FastAPI or Django
- PostgreSQL
- Docker
- AWS
- REST APIs
- 2+ years of experience
"""

RESUME = """
Name: Rahul Sharma

Experience:
3 years as a Software Developer.

Skills:
Python, FastAPI, MySQL, Docker, REST APIs, Git

Projects:
Built a food delivery backend using FastAPI and MySQL.
Deployed application using Docker.
"""


def ask_llm(system_prompt, user_prompt):
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )

    answer = response.choices[0].message.content
    return answer


def step1_res_extract():
    system_prompt = """
You are a professional HR assistant.
Extract only the skills explicitly mentioned in the resume.
Do not invent any skills.
Return only the extracted skills.
"""

    user_prompt = f"""
Extract the skills from this resume:

{RESUME}
"""

    return ask_llm(system_prompt, user_prompt)


def step2_res_extract():
    system_prompt = """
You are a professional HR assistant.
Extract the skills and experience requirements
from the job description.
Do not invent any requirements.
Return only the extracted requirements.
"""

    user_prompt = f"""
Extract the requirements from this job description:

{JD}
"""

    return ask_llm(system_prompt, user_prompt)


def step3_match(candidate, jd):
    system_prompt = """
You are a professional HR assistant.

Compare the candidate's skills with the job requirements.
Return:
1. Match score out of 100.
2. Matching skills.
3. Missing skills.
4. Short hiring-fit verdict with reasoning.

Do not invent candidate skills or experience.
Explain that the score is an estimate, not a hiring decision.
"""

    user_prompt = f"""
Compare the candidate and job requirements.

Job requirements:
{jd}

Candidate skills and experience:
{candidate}
"""

    return ask_llm(system_prompt, user_prompt)


candidate = step1_res_extract()
print("Candidate Skills:")
print(candidate)
 

jd = step2_res_extract()
print("\nJob Requirements:")
print(jd)
 
score = step3_match(candidate, jd)
print("\nResume Analysis:")
print(score)
