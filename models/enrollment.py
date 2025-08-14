from pydantic import BaseModel
from datetime import datetime

class Enrollment(BaseModel):
    student_id: str
    course_id: str
    enrolled_at: datetime = datetime.utcnow()  # Default timestamp

class EnrollmentResponse(Enrollment):
    id: str
