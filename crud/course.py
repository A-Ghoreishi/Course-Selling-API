from database import mongodb

def get_collection():
    if not mongodb.db:
        raise Exception("Database not connected yet!")
    return mongodb.db["courses"]

async def get_all():
    return await get_collection().find().to_list(100)

async def get_one(course_id):
    return await get_collection().find_one({"_id": course_id})

async def create(data):
    result = await get_collection().insert_one(data)
    return str(result.inserted_id)

async def update(course_id, update_data):
    await get_collection().update_one({"_id": course_id}, {"$set": update_data})
    return await get_one(course_id)

async def delete(course_id):
    await get_collection().delete_one({"_id": course_id})
    return {"status": "deleted"}
