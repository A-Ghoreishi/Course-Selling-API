from fastapi import APIRouter, HTTPException
from models.course import Course
import crud.course as course_crud

router = APIRouter(prefix="/courses", tags=["Courses"])

# List all courses
@router.get("/")
async def get_courses():
    return await course_crud.list_courses()

# Create a course
@router.post("/")
async def add_course(course: Course):
    return await course_crud.create_course(course.dict())

# Get course by ID
@router.get("/{id}")
async def get_course(id: str):
    course = await course_crud.get_course(id)
    if course:
        return course
    raise HTTPException(status_code=404, detail="Course not found")

# Update course
@router.put("/{id}")
async def update_course(id: str, course: Course):
    updated = await course_crud.update_course(id, course.dict())
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="Course not found")

# Delete course
@router.delete("/{id}")
async def delete_course(id: str):
    result = await course_crud.delete_course(id)
    if result["deleted_count"]:
        return {"message": "Course deleted"}
    raise HTTPException(status_code=404, detail="Course not found")

# Get all courses by instructor
@router.get("/instructor/{instructor_id}")
async def get_courses_by_instructor(instructor_id: str):
    return await course_crud.get_courses_by_instructor(instructor_id)
