from fastapi import FastAPI,APIRouter,Request,HTTPException,status
from app.routes.task import task
from app.routes.user import user




app=FastAPI()
app.include_router(task)
app.include_router(user)



@app.get("/home")
def get_home(request: Request):
    return {"message": "Connected!"}


