from fastapi import FastAPI
from database import connect_db, close_db
from routers.instructor import router as instructor_router

app = FastAPI(title="Course Selling API")

@app.on_event("startup")
async def startup():
    connect_db()

@app.on_event("shutdown")
async def shutdown():
    close_db()

@app.get("/")
async def root():
    return {"message: Course Selling API is running"}

app.include_router(instructor_router)
# app.include_router(student.router)
# app.include_router(course.router)
# app.include_router(enrollment.router)
