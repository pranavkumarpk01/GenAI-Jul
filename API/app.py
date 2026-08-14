#Library -> Predefined fucntions which has to be downloaded into our system to use it..
#we have multiple frameworks which will help us to develop apis..Fast API
#Whenever you are developing a python based applciation its mandatory to have a requirements.txt file which is responsible to hold all your libraries
#Once u have all the libraires mentioned in that file, we have to install using pip install -r requirements.txt
#inorder to use the mongo db databse, u need to run a docker continaer with the command   docker run --name my-mongo -d -p 27017:27017 mongo:latest
#It is mandatory to download docker before running the above command


from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI(
    title="Student CRUD Operation",
    description="Simple CRUD API using FastAPI and Mongo",
    version="1.0"
)

#You have to establish the connection with the db
client = MongoClient("mongodb://localhost:27017/")
db = client["training_db"]
collection = db["students"]

@app.post("/students")
def create_student(student : dict):
    result = collection.insert_one(student)

    return{
        "message":"student data has been created",
        "_id" : str(result.inserted_id)
    }




@app.get("/students/get")
def get_students():
    students=[]
    for student in collection.find():
        student["_id"]=str(student["_id"])
        students.append(student)

    return students    


@app.put("/students/{student_id}")
def update_student(student_id:str , student:dict):
    result = collection.update_one(
        {"_id":ObjectId(student_id)},
        {"$set":student}
    )

    return{
        "message":"student updated"
    }

@app.delete("/students/{student_id}")
def delete_student(student_id:str):
    result =collection.delete_one(
       {"_id": ObjectId(student_id)}
    )
    return{
        "message":"Student data deleted"
    }

#  {"$set":student}
# $set:{
#   "course": "DevOps"
# }

#delete one particular column