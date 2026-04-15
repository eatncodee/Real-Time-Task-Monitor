from fastapi import FastAPI,APIRouter,Request,HTTPException,status, Depends
from app.schema.schema import Task,User,TaskUpdate
from app.Oauth2 import get_current_user
from app.db.db import db,tasks,users
from datetime import datetime
from bson import ObjectId


task=APIRouter(tags=['Tasks'])


@task.get("/alltasks")
def get_tasks(current_user: str = Depends(get_current_user)):
    task_list=list(tasks.find({"email": current_user["email"]},{"_id":0}))
    return{"messge":"hi","tasks":task_list}
    
@task.post("/task")
def add_tasks(task:Task, current_user: str = Depends(get_current_user)):
    task_dict=task.model_dump()
    task_dict["email"]=current_user["email"]
    task_dict["Created_at"] = datetime.now()
    result = tasks.insert_one(task_dict)
    return {"messge":"done","id":str(result.inserted_id)}

@task.put("/tasks/{id}")
def update_task(task:TaskUpdate,id:str, current_user : str = Depends(get_current_user)):
    obj_id = ObjectId(id)

    result = tasks.find_one_and_update(
        {"_id" : obj_id, "email" : current_user["email"]},
        {'$set': task.model_dump(exclude_none=True)}, 
        return_document=ReturnDocument.AFTER
    )
    if result:
        result["_id"]=str(result["_id"])
        return result

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found, try again")


@task.delete("/tasks/{id}")
def delete_task(id : str, current_user : str = Depends(get_current_user)):
    obj_id=ObjectId(id)

    result=tasks.find_one_and_delete({"_id" : obj_id, "email" : current_user["email"]})

    if result:
        result["_id"]=str(result["_id"])
        return {"Message":"Deleted", "Task: ": result}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found, try again")


