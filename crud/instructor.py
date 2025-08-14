# crud/instructor.py
from bson import ObjectId
from database import db

# Create a new instructor in the database
async def create_instructor(data: dict):
    result = await db.instructors.insert_one(data)  # Insert into MongoDB
    return await db.instructors.find_one({"_id": result.inserted_id})  # Return saved instructor

# Get a list of all instructors
async def list_instructors():
    instructors = await db.instructors.find().to_list(100)  # Convert cursor to list
    return instructors

# Get a single instructor by ID
async def get_instructor(id: str):
    instructor = await db.instructors.find_one({"_id": ObjectId(id)})
    return instructor

# Update an instructor's data
async def update_instructor(id: str, data: dict):
    await db.instructors.update_one({"_id": ObjectId(id)}, {"$set": data})
    return await get_instructor(id)  # Return updated instructor

# Delete an instructor by ID
async def delete_instructor(id: str):
    result = await db.instructors.delete_one({"_id": ObjectId(id)})
    return {"deleted_count": result.deleted_count}  # Return how many were deleted
