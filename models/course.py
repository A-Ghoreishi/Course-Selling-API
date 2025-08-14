from pydantic import BaseModel
from typing import Optional

class Course(BaseModel):
    title: str           # Course title
    description: str     # Short description
    instructor_id: str   # ID of the instructor who owns this course
    price: Optional[float] = 0.0  # Optional price

# Optional: You can create a response model with ID
class CourseResponse(Course):
    id: str
