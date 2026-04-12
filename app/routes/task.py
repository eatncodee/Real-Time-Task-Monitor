from fastapi import FastAPI,APIRouter,Request,HTTPException,status
from app.schema.schema import Task,User
from app.db.db import db,collection,users


task=APIRouter()


@task.get("/alltasks")
def get_tasks():
    gg=list(collection.find({},{"_id":0}))
    return{"messge":"hi","tasks":gg}
    
@task.post("/todo")
def add_tasks(task:Task):
    task_dict=task.model_dump()
    collection.insert_one(task_dict)
    return {"messge":"done"}