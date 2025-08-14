from fastapi import APIRouter, HTTPException
from crud import instructor as instructor_crud
from pydantic import BaseModel
from bson import ObjectId

router = APIRouter(prefix="/instructors", tags=["Instructors"])

class InstructorCreate(BaseModel):
    name: str
    email: str
    courses: list[str] = []

class InstructorUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    courses: list[str] | None = None

def validate_object_id(id_str: str) -> str:
    try:
        return str(ObjectId(id_str))
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

@router.get("/")
async def get_instructors():
    return await instructor_crud.get_all()

@router.get("/{instructor_id}")
async def get_instructor(instructor_id: str):
    instructor_id = validate_object_id(instructor_id)
    instructor = await instructor_crud.get_one(instructor_id)
    if not instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return instructor

@router.post("/")
async def create_instructor(data: InstructorCreate):
    return await instructor_crud.create(data.dict())

@router.put("/{instructor_id}")
async def update_instructor(instructor_id: str, data: InstructorUpdate):
    instructor_id = validate_object_id(instructor_id)
    updated = await instructor_crud.update(instructor_id, data.dict(exclude_none=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return updated

@router.delete("/{instructor_id}")
async def delete_instructor(instructor_id: str):
    instructor_id = validate_object_id(instructor_id)
    return await instructor_crud.delete(instructor_id)
