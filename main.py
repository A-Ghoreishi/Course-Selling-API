from fastapi import FastAPI
from database import connect_to_mongo, close_mongo_connection
from routers import instructor, student, course, enrollment
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()          # ensures db is ready before any route runs
    try:
        yield
    finally:
        await close_mongo_connection()

app = FastAPI(lifespan=lifespan)

# Include routers
app.include_router(student.router,     prefix="/students",     tags=["students"])
app.include_router(instructor.router,  prefix="/instructors",  tags=["instructors"])
app.include_router(course.router,      prefix="/courses",      tags=["courses"])
app.include_router(enrollment.router,  prefix="/enrollments",  tags=["enrollments"])

@app.get("/")
async def root():
    return {"message": "Course Selling API is running!"}


#uvicorn main:app --reload
