from database import db
from bson import ObjectId

collection = db["students"]

async def list_students():
    return list(collection.find())

async def create_student(data):
    result = collection.insert_one(data)
    return str(result.inserted_id)

async def get_student(id):
    return collection.find_one({"_id": ObjectId(id)})

async def update_student(id, data):
    collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    return get_student(id)

async def delete_student(id):
    return collection.delete_one({"_id": ObjectId(id)})
