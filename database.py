from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional

client: Optional[AsyncIOMotorClient] = None
db = None

MONGO_URI = "mongodb://localhost:27017" 
DB_NAME = "course_selling_db"             

def connect_db():
    global client, db
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DB_NAME]

def close_db():
    global client
    if client:
        client.close()
