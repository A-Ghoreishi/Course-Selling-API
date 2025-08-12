from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional

client: Optional[AsyncIOMotorClient] = None
db = None

def connect_db():
    global client, db
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client.course_selling_db

def close_db():
    global client
    if client:
        client.close()
