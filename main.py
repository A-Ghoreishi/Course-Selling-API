from fastapi import FastAPI
from database import mongodb
from routers import instructor, student, course, enrollment
from contextlib import asynccontextmanager

# Lifespan context
@asynccontextmanager
async def lifespan(app: FastAPI):
    await mongodb.connect()
    yield
    await mongodb.close()

app = FastAPI(title="Course Selling API", lifespan=lifespan)

# Include routers
app.include_router(instructor.router)
app.include_router(student.router)
app.include_router(course.router)
app.include_router(enrollment.router)

@app.get("/")
async def root():
    return {"message": "Course Selling API is running!"}
