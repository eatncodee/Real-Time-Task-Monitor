from pydantic import BaseModel,EmailStr
class Task(BaseModel):
    user:str
    task:str
    completed:bool =False

class User(BaseModel):
    email:EmailStr
    password:str


class Logincreds(BaseModel):
    email:EmailStr
    password:str