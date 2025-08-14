from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name: str        # Student name
    email: str       # Student email
    age: Optional[int] = None  # Optional age

class StudentResponse(Student):
    id: str
