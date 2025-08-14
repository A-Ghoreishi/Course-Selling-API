from fastapi import APIRouter, HTTPException
from models.student import Student
import crud.student as student_crud

router = APIRouter(prefix="/students", tags=["Students"])

# List all students
@router.get("/")
async def get_students():
    return await student_crud.list_students()

# Create a student
@router.post("/")
async def add_student(student: Student):
    return await student_crud.create_student(student.dict())

# Get student by ID
@router.get("/{id}")
async def get_student(id: str):
    student = await student_crud.get_student(id)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")

# Update student
@router.put("/{id}")
async def update_student(id: str, student: Student):
    updated = await student_crud.update_student(id, student.dict())
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="Student not found")

# Delete student
@router.delete("/{id}")
async def delete_student(id: str):
    result = await student_crud.delete_student(id)
    if result["deleted_count"]:
        return {"message": "Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found")
