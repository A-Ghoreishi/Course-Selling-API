from fastapi import APIRouter, HTTPException
from crud import course as course_crud
from pydantic import BaseModel
from bson import ObjectId

router = APIRouter(prefix="/courses", tags=["Courses"])

class CourseCreate(BaseModel):
    title: str
    description: str
    price: float
    instructor_id: str

class CourseUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    price: float | None = None
    instructor_id: str | None = None

def validate_object_id(id_str: str) -> str:
    try:
        return str(ObjectId(id_str))
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

@router.get("/")
async def get_courses():
    return await course_crud.get_all()

@router.get("/{course_id}")
async def get_course(course_id: str):
    course_id = validate_object_id(course_id)
    course = await course_crud.get_one(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.post("/")
async def create_course(data: CourseCreate):
    return await course_crud.create(data.dict())

@router.put("/{course_id}")
async def update_course(course_id: str, data: CourseUpdate):
    course_id = validate_object_id(course_id)
    updated = await course_crud.update(course_id, data.dict(exclude_none=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Course not found")
    return updated

@router.delete("/{course_id}")
async def delete_course(course_id: str):
    course_id = validate_object_id(course_id)
    return await course_crud.delete(course_id)
