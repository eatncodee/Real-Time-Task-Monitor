import os
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi





load_dotenv()
connection=os.getenv("mongo_uri")
client=MongoClient(connection,tlsCAFile=certifi.where())
db=client.task_db
collection=db.task_collection
users=db.users
