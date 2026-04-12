from fastapi import APIRouter, Depends, status, HTTPException,Response
from app.db.db import db,collection,users
from app.utils.hash import verify
from pydantic import EmailStr
from app.schema.schema import Logincreds
from app import Oauth2

auth=APIRouter(tags=['Authentication'])


@auth.post("/login")
def login(creds:Logincreds):
    user=users.find_one({"email":creds.email})

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    if not verify(creds.password,user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials")    

    token=Oauth2.create_access_token(data={"email" : user["email"]})

    return {"token": token, "token_type":"bearer"}


