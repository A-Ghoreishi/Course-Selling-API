from database import mongodb

def get_collection():
    if not mongodb.db:
        raise Exception("Database not connected yet!")
    return mongodb.db["instructors"]

async def get_all():
    return await get_collection().find().to_list(100)

async def get_one(instructor_id):
    return await get_collection().find_one({"_id": instructor_id})

async def create(data):
    result = await get_collection().insert_one(data)
    return str(result.inserted_id)

async def update(instructor_id, update_data):
    await get_collection().update_one({"_id": instructor_id}, {"$set": update_data})
    return await get_one(instructor_id)

async def delete(instructor_id):
    await get_collection().delete_one({"_id": instructor_id})
    return {"status": "deleted"}
