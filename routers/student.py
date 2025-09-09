from fastapi import APIRouter, HTTPException
from crud.student import create_student
from pydantic import BaseModel
from bson import ObjectId

router = APIRouter()

class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: str

@router.post("/", status_code=201)
async def add_student(payload: StudentCreate):
    doc = payload.model_dump()
    created = await create_student(doc)
    return created


# class StudentCreate(BaseModel):
#     name: str
#     email: str

# class StudentUpdate(BaseModel):
#     name: str | None = None
#     email: str | None = None

# def validate_object_id(id_str: str) -> str:
#     try:
#         return str(ObjectId(id_str))
#     except Exception:
#         raise HTTPException(status_code=400, detail="Invalid ID format")

# @router.get("/")
# async def get_students():
#     return await student_crud.get_all()

# @router.get("/{student_id}")
# async def get_student(student_id: str):
#     student_id = validate_object_id(student_id)
#     student = await student_crud.get_one(student_id)
#     if not student:
#         raise HTTPException(status_code=404, detail="Student not found")
#     return student

# @router.post("/")
# async def create_student(data: StudentCreate):
#     return await student_crud.create(data.dict())

# @router.put("/{student_id}")
# async def update_student(student_id: str, data: StudentUpdate):
#     student_id = validate_object_id(student_id)
#     updated = await student_crud.update(student_id, data.dict(exclude_none=True))
#     if not updated:
#         raise HTTPException(status_code=404, detail="Student not found")
#     return updated

# @router.delete("/{student_id}")
# async def delete_student(student_id: str):
#     student_id = validate_object_id(student_id)
#     return await student_crud.delete(student_id)
