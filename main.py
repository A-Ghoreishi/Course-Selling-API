from fastapi import FastAPI
from database import connect_db, close_db
from routers import instructor, course, student, enrollment

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

app.include_router(instructor.router, prefix="/instructors", tags=["Instructors"])
app.include_router(course.router, prefix="/courses", tags=["Courses"])
app.include_router(student.router, prefix="/students", tags=["Students"])
app.include_router(enrollment.router, prefix="/enrollments", tags=["Enrollments"])
