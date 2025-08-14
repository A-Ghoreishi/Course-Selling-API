from database import db
from bson import ObjectId

collection = db["enrollments"]

async def list_enrollments():
    return list(collection.find())

async def enroll_student(data):
    result = collection.insert_one(data)
    return str(result.inserted_id)

async def delete_enrollment(id):
    return collection.delete_one({"_id": ObjectId(id)})

async def get_courses_of_student(student_id):
    return list(collection.find({"student_id": student_id}))

async def get_students_of_course(course_id):
    return list(collection.find({"course_id": course_id}))
