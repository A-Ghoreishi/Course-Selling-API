# routers/instructor.py
from fastapi import APIRouter, HTTPException
from models.instructor import Instructor
import crud.instructor as instructor_crud

# Create a router for all instructor endpoints
router = APIRouter(prefix="/instructors", tags=["Instructors"])

# Create a new instructor
@router.post("/")
async def add_instructor(instructor: Instructor):
    result = await instructor_crud.create_instructor(instructor.dict())  # Save to DB
    return result

# Get all instructors
@router.get("/")
async def get_instructors():
    return await instructor_crud.list_instructors()

# Get a single instructor by ID
@router.get("/{id}")
async def get_instructor(id: str):
    instructor = await instructor_crud.get_instructor(id)
    if instructor:
        return instructor
    raise HTTPException(status_code=404, detail="Instructor not found")

# Update an instructor by ID
@router.put("/{id}")
async def update_instructor(id: str, instructor: Instructor):
    updated = await instructor_crud.update_instructor(id, instructor.dict())
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="Instructor not found")

# Delete an instructor by ID
@router.delete("/{id}")
async def delete_instructor(id: str):
    result = await instructor_crud.delete_instructor(id)
    if result["deleted_count"]:
        return {"message": "Instructor deleted"}
    raise HTTPException(status_code=404, detail="Instructor not found")
