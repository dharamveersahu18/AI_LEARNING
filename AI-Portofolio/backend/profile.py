import json
from pathlib import Path

from pydantic import BaseModel, Field, ValidationError

# 1. define the structure of education
class Education(BaseModel):
  degree: str
  college: str
  location: str
  start_year: int
  expected_graduation: int
  cgpa: float = Field(ge=0, le=10)

  # 2. define the structure of each project
class Project(BaseModel):
    name: str
    description: str
    technologies: list[str]

# 3. Define social links
class SocialLinks(BaseModel):
    github: str
    linkedin: str 
    leetcode: str

# 4. Define the complete Candidate  profile

class CandidateProfile(BaseModel):
  name: str
  role: str
  education: Education
  skills: list[str]
  projects: list[Project]
  experience: list[str]
  achievements: list[str]
  certifications: list[str]
  social_links: SocialLinks

# 5. Load candidate json
PROFILE_PATH = Path(__file__).parent / "candidate.json"

def load_candidate_profile()-> CandidateProfile:
  with PROFILE_PATH.open("r", encoding="utf-8") as file:
    raw_data = json.load(file)
  return CandidateProfile.model_validate(raw_data)

# 6. Test the Profile
if __name__ == "__main__":
    try:
       candidate = load_candidate_profile()
       print("candidate profile is valid!\n")
       print(candidate.model_dump_json(indent=2))

    except FileNotFoundError:
       print(f"Profile file not found:{PROFILE_PATH}")

    except json.JSONDecodeError as error:
       print(f"Invalid JSON: {error}")

    except ValidationError as error:
       print("Profile validation failed: ")
       print(error)
    