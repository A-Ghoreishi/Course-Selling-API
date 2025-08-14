from pydantic import BaseModel, Field
from typing import Optional

class Course(BaseModel):
    title: str = Field(..., example="Python for Beginners")
    description: Optional[str] = Field(None, example="Learn Python from scratch")
    instructor_id: str = Field(..., example="instructor123")
    price: float = Field(..., example=49.99)
