from fastapi import FastAPI,APIRouter,Request,HTTPException,status
from app.routes.task import task
from app.routes.user import user
from app.routes.auth import auth



app=FastAPI()
app.include_router(task)
app.include_router(user)
app.include_router(auth)
app.include_router(ws)

@app.get("/home")
def get_home(request: Request):
    return {"message": "Connected!"}


