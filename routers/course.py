# routers/course.py
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Optional
from crud.course import (
    create_course, get_course_by_id, list_courses,
    update_course, delete_course
)

router = APIRouter()

class CourseCreate(BaseModel):
    code: str = Field(..., examples=["CS101"])
    title: str
    credits: int = Field(ge=0, le=10)
    instructor_id: Optional[str] = None  # store as ObjectId string
    description: Optional[str] = None

class CourseUpdate(BaseModel):
    code: Optional[str] = None
    title: Optional[str] = None
    credits: Optional[int] = Field(default=None, ge=0, le=10)
    instructor_id: Optional[str] = None
    description: Optional[str] = None

@router.post("/", status_code=201)
async def add_course(payload: CourseCreate):
    return await create_course(payload.model_dump())

@router.get("/")
async def get_courses(skip: int = Query(0, ge=0), limit: int = Query(50, ge=1, le=200)):
    return await list_courses(skip=skip, limit=limit)

@router.get("/{course_id}")
async def get_course(course_id: str):
    from bson import ObjectId
    if not ObjectId.is_valid(course_id):
        raise HTTPException(400, "Invalid course id")
    found = await get_course_by_id(course_id)
    if not found:
        raise HTTPException(404, "Course not found")
    return found

@router.patch("/{course_id}")
async def patch_course(course_id: str, payload: CourseUpdate):
    from bson import ObjectId
    if not ObjectId.is_valid(course_id):
        raise HTTPException(400, "Invalid course id")
    updated = await update_course(course_id, {k: v for k, v in payload.model_dump().items() if v is not None})
    if not updated:
        raise HTTPException(404, "Course not found")
    return updated

@router.delete("/{course_id}", status_code=204)
async def remove_course(course_id: str):
    from bson import ObjectId
    if not ObjectId.is_valid(course_id):
        raise HTTPException(400, "Invalid course id")
    ok = await delete_course(course_id)
    if not ok:
        raise HTTPException(404, "Course not found")
