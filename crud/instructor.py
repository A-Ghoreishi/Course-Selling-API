# crud/instructor.py
from typing import Optional, List, Dict, Any
from bson import ObjectId
from database import get_collection
from utils.serialize import serialize_doc

def _oid(id: str) -> ObjectId:
    if not ObjectId.is_valid(id):
        raise ValueError("Invalid ObjectId")
    return ObjectId(id)

async def create_instructor(data: Dict[str, Any]) -> dict:
    coll = get_collection("instructors")
    result = await coll.insert_one(data)
    created = await coll.find_one({"_id": result.inserted_id})
    return serialize_doc(created)

async def get_instructor_by_id(instructor_id: str) -> Optional[dict]:
    coll = get_collection("instructors")
    doc = await coll.find_one({"_id": _oid(instructor_id)})
    return serialize_doc(doc)

async def list_instructors(skip: int = 0, limit: int = 50) -> List[dict]:
    coll = get_collection("instructors")
    cursor = coll.find({}, skip=skip, limit=limit).sort("_id", 1)
    return [serialize_doc(d) async for d in cursor]

async def update_instructor(instructor_id: str, data: Dict[str, Any]) -> Optional[dict]:
    coll = get_collection("instructors")
    await coll.update_one({"_id": _oid(instructor_id)}, {"$set": data})
    return await get_instructor_by_id(instructor_id)

async def delete_instructor(instructor_id: str) -> bool:
    coll = get_collection("instructors")
    res = await coll.delete_one({"_id": _oid(instructor_id)})
    return res.deleted_count == 1
