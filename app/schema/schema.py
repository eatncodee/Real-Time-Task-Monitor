from pydantic import BaseModel,EmailStr
from typing import Optional
class Task(BaseModel):
    task:str
    completed:bool =False

class User(BaseModel):
    email:EmailStr
    password:str


class Logincreds(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    type:str

class TokenData(BaseModel):
    email:Optional[EmailStr]= None
