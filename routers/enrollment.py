from fastapi import APIRouter, HTTPException
from models.enrollment import Enrollment
import crud.enrollment as enrollment_crud

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

# List all enrollments
@router.get("/")
async def get_enrollments():
    return await enrollment_crud.list_enrollments()

# Enroll a student
@router.post("/")
async def enroll_student(enrollment: Enrollment):
    return await enrollment_crud.enroll_student(enrollment.dict())

# Remove enrollment
@router.delete("/{id}")
async def remove_enrollment(id: str):
    result = await enrollment_crud.delete_enrollment(id)
    if result["deleted_count"]:
        return {"message": "Enrollment removed"}
    raise HTTPException(status_code=404, detail="Enrollment not found")

# Get student's courses
@router.get("/student/{student_id}")
async def student_courses(student_id: str):
    return await enrollment_crud.get_courses_of_student(student_id)

# Get course's students
@router.get("/course/{course_id}")
async def course_students(course_id: str):
    return await enrollment_crud.get_students_of_course(course_id)
