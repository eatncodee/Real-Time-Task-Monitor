from fastapi import FastAPI,APIRouter,Request,HTTPException,status
import typing 
from bson import ObjectId
from passlib.context import CryptContext
from app.schema.schema import Task,User
from app.db.db import db,collection,users

user=APIRouter()

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")


@user.post("/user")
def create(user:User):
    existing_user = db.users.find_one({"email": user.email})
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered. Please log in."
        )
    hashed_pass=pwd_context.hash(user.password)
    user.password=hashed_pass
    result=users.insert_one(user.model_dump())
    return {"message":f"user create with id :{result.inserted_id}"}

@user.get("/user/{id}")
def info(id:str):
    try:
        obj_id = ObjectId(id) 
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid User ID format"
        )
    result = db.users.find_one({"_id": obj_id})
    
    if result:
        result["_id"] = str(result["_id"]) 
        return result        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )