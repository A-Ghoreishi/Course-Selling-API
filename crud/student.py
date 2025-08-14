from database import mongodb

def get_collection():
    if not mongodb.db:
        raise Exception("Database not connected yet!")
    return mongodb.db["students"]

async def get_all():
    return await get_collection().find().to_list(100)

async def get_one(student_id):
    return await get_collection().find_one({"_id": student_id})

async def create(data):
    result = await get_collection().insert_one(data)
    return str(result.inserted_id)

async def update(student_id, update_data):
    await get_collection().update_one({"_id": student_id}, {"$set": update_data})
    return await get_one(student_id)

async def delete(student_id):
    await get_collection().delete_one({"_id": student_id})
    return {"status": "deleted"}
