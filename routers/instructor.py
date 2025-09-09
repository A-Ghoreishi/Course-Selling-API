# routers/instructor.py
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from crud.instructor import (
    create_instructor, get_instructor_by_id, list_instructors,
    update_instructor, delete_instructor
)

router = APIRouter()

class InstructorCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    department: Optional[str] = None

class InstructorUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    department: Optional[str] = None

@router.post("/", status_code=201)
async def add_instructor(payload: InstructorCreate):
    return await create_instructor(payload.model_dump())

@router.get("/", response_model=list[dict])
async def get_instructors(skip: int = Query(0, ge=0), limit: int = Query(50, ge=1, le=200)):
    return await list_instructors(skip=skip, limit=limit)

@router.get("/{instructor_id}")
async def get_instructor(instructor_id: str):
    try:
        found = await get_instructor_by_id(instructor_id)
    except ValueError:
        raise HTTPException(400, "Invalid instructor id")
    if not found:
        raise HTTPException(404, "Instructor not found")
    return found

@router.patch("/{instructor_id}")
async def patch_instructor(instructor_id: str, payload: InstructorUpdate):
    try:
        updated = await update_instructor(instructor_id, {k: v for k, v in payload.model_dump().items() if v is not None})
    except ValueError:
        raise HTTPException(400, "Invalid instructor id")
    if not updated:
        raise HTTPException(404, "Instructor not found")
    return updated

@router.delete("/{instructor_id}", status_code=204)
async def remove_instructor(instructor_id: str):
    try:
        ok = await delete_instructor(instructor_id)
    except ValueError:
        raise HTTPException(400, "Invalid instructor id")
    if not ok:
        raise HTTPException(404, "Instructor not found")
