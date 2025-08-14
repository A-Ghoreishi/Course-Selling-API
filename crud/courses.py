from database import db  # MongoDB connection
from bson import ObjectId

collection = db["courses"]  # MongoDB collection

async def list_courses():
    return list(collection.find())

async def create_course(data):
    result = collection.insert_one(data)
    return str(result.inserted_id)

async def get_course(id):
    return collection.find_one({"_id": ObjectId(id)})

async def update_course(id, data):
    collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return get_course(id)

async def delete_course(id):
    return collection.delete_one({"_id": ObjectId(id)})

async def get_courses_by_instructor(instructor_id):
    return list(collection.find({"instructor_id": instructor_id}))
