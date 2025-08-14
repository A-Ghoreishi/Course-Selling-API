from database import mongodb

def get_collection():
    if not mongodb.db:
        raise Exception("Database not connected yet!")
    return mongodb.db["enrollments"]

async def get_all():
    return await get_collection().find().to_list(100)

async def get_one(enrollment_id):
    return await get_collection().find_one({"_id": enrollment_id})

async def create(data):
    result = await get_collection().insert_one(data)
    return str(result.inserted_id)

async def update(enrollment_id, update_data):
    await get_collection().update_one({"_id": enrollment_id}, {"$set": update_data})
    return await get_one(enrollment_id)

async def delete(enrollment_id):
    await get_collection().delete_one({"_id": enrollment_id})
    return {"status": "deleted"}
