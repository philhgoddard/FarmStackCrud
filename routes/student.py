from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntity
from bson import ObjectId

student_router = APIRouter()

#create endpoints

# the decorator receives the http request type: get,post,put,delete
# and the URL includes the path and content passed from the client
# each route runs the async function with a descriptive name -
# the body of the function uses a connection to mongo and a mongo function to the db
# some mongo functions pass in data, e.g. ids to access specific documents
# the return returns the response from the db function call
# the return responses are passed back to the UI

# the get route calls database for list of students
@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntity(connection.local.student.find())

@student_router.get('/hello')
async def hell_world():
    return "Hello world"

# get route with a student ID returns one student with matching ID
# using find_one()
@student_router.get('/students/{studentID')
async def find_study_by_id(studentId):
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

# Post creates a new student by passing a key:value dict object for a student
# and returns all students using find() function after insert_one in db
@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())

# Put updates a student by receiving the student ID in request and search for that student in my db
# here we also get the whole student in the body of the request
@student_router.put('/students/{studentID}')
async def update_student(studentId, student: Student):
    #use mongo method to fina and update student data
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(studentId)},
        {"$set": dict(student)}
    )
    # return is wrapped in schema in the format we want it for the UI
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

#delete a student, we only need a student id
@student_router.delete('/students/{studentId}')
async def delete_student(studentId):
# find student and deletes it and returns the same student object
    return studentEntity(connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)}))
