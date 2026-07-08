from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["youtube_manager_db"]
users_collection = db["users"]

for user in users_collection.find():
    print(user)