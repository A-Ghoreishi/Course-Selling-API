from pydantic import BaseModel, EmailStr

class Instructor(BaseModel):
    name : str
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com"
            }
        }