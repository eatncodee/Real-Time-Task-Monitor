from fastapi import FastAPI,APIRouter,Request,HTTPException,status, Depends
from app.schema.schema import Task,User
from app.Oauth2 import get_current_user
from app.db.db import db,tasks,users


task=APIRouter(tags=['Tasks'])


@task.get("/alltasks")
def get_tasks(current_user: str = Depends(get_current_user)):
    task_list=list(tasks.find({"email": current_user["email"]},{"_id":0}))
    return{"messge":"hi","tasks":task_list}
    
@task.post("/todo")
def add_tasks(task:Task, current_user: str = Depends(get_current_user)):
    task_dict=task.model_dump()
    task_dict["email"]=current_user["email"]
    tasks.insert_one(task_dict)
    return {"messge":"done"}