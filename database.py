from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "course_selling_db"

class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.uri = uri
        self.db_name = db_name
        self.client: Optional[AsyncIOMotorClient] = None
        self.db = None

    async def connect(self):
        self.client = AsyncIOMotorClient(self.uri)
        self.db = self.client[self.db_name]
        # Test connection
        try:
            await self.client.admin.command("ping")
            print("✅ MongoDB connected successfully!")
        except Exception as e:
            print("❌ MongoDB connection failed:", e)

    async def close(self):
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")

# Create a single MongoDB instance
mongodb = MongoDB(MONGO_URI, DB_NAME)
