# crud/student.py
from typing import Optional, List, Dict, Any
from bson import ObjectId
from database import get_collection
from utils.serialize import serialize_doc

def _oid(id: str) -> ObjectId:
    from bson import ObjectId
    if not ObjectId.is_valid(id):
        raise ValueError("Invalid ObjectId")
    return ObjectId(id)

async def create_student(data: Dict[str, Any]) -> dict:
    coll = get_collection("students")
    result = await coll.insert_one(data)
    # fetch the created doc so we return a consistent, serialized document
    created = await coll.find_one({"_id": result.inserted_id})
    return serialize_doc(created)

async def get_student_by_id(student_id: str) -> Optional[dict]:
    coll = get_collection("students")
    doc = await coll.find_one({"_id": _oid(student_id)})
    return serialize_doc(doc)

async def list_students(skip: int = 0, limit: int = 50) -> List[dict]:
    coll = get_collection("students")
    cursor = coll.find({}, skip=skip, limit=limit).sort("_id", 1)
    return [serialize_doc(d) async for d in cursor]

async def update_student(student_id: str, data: Dict[str, Any]) -> Optional[dict]:
    coll = get_collection("students")
    await coll.update_one({"_id": _oid(student_id)}, {"$set": data})
    return await get_student_by_id(student_id)

async def delete_student(student_id: str) -> bool:
    coll = get_collection("students")
    res = await coll.delete_one({"_id": _oid(student_id)})
    return res.deleted_count == 1


# def get_collection():
#     if not mongodb.db:
#         raise Exception("Database not connected yet!")
#     return mongodb.db["students"]

# async def get_all():
#     return await get_collection().find().to_list(100)

# async def get_one(student_id):
#     return await get_collection().find_one({"_id": student_id})

# async def create(data):
#     result = await get_collection().insert_one(data)
#     return str(result.inserted_id)

# async def update(student_id, update_data):
#     await get_collection().update_one({"_id": student_id}, {"$set": update_data})
#     return await get_one(student_id)

# async def delete(student_id):
#     await get_collection().delete_one({"_id": student_id})
#     return {"status": "deleted"}
