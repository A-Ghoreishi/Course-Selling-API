from fastapi import APIRouter, HTTPException
from crud import enrollment as enrollment_crud
from pydantic import BaseModel
from bson import ObjectId

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

class EnrollmentCreate(BaseModel):
    student_id: str
    course_id: str

class EnrollmentUpdate(BaseModel):
    student_id: str | None = None
    course_id: str | None = None

def validate_object_id(id_str: str) -> str:
    try:
        return str(ObjectId(id_str))
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

@router.get("/")
async def get_enrollments():
    return await enrollment_crud.get_all()

@router.get("/{enrollment_id}")
async def get_enrollment(enrollment_id: str):
    enrollment_id = validate_object_id(enrollment_id)
    enrollment = await enrollment_crud.get_one(enrollment_id)
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return enrollment

@router.post("/")
async def create_enrollment(data: EnrollmentCreate):
    return await enrollment_crud.create(data.dict())

@router.put("/{enrollment_id}")
async def update_enrollment(enrollment_id: str, data: EnrollmentUpdate):
    enrollment_id = validate_object_id(enrollment_id)
    updated = await enrollment_crud.update(enrollment_id, data.dict(exclude_none=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return updated

@router.delete("/{enrollment_id}")
async def delete_enrollment(enrollment_id: str):
    enrollment_id = validate_object_id(enrollment_id)
    return await enrollment_crud.delete(enrollment_id)
