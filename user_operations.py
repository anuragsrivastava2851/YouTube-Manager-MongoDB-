from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os

# Connect to the database
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["youtube_manager_db"]
users_collection = db["users"]



def create_user(username, email):
    new_user = {
        "username": username,
        "email": email,
        "created_at": datetime.now()
    }
    result = users_collection.insert_one(new_user)
    print("User created with ID:", result.inserted_id)
    return result.inserted_id



def get_all_users():
    print("\n--- All Users ---")
    for user in users_collection.find():
        print(user)


def get_user_by_username(username):
    user = users_collection.find_one({"username": username})
    if user:
        print("\nUser found:", user)
    else:
        print("\nNo user found with that username.")
    return user



def update_user_email(username, new_email):
    result = users_collection.update_one(
        {"username": username},
        {"$set": {"email": new_email}}
    )
    if result.matched_count > 0:
        print(f"\nUpdated {username}'s email to {new_email}")
    else:
        print("\nNo user found to update.")



def delete_user(username):
    result = users_collection.delete_one({"username": username})
    if result.deleted_count > 0:
        print(f"\nDeleted user: {username}")
    else:
        print("\nNo user found to delete.")


# ---------- Testing the functions ----------
if __name__ == "__main__":
    get_all_users()
    create_user("testuser", "testuser@example.com")
    get_user_by_username("testuser")
    update_user_email("testuser", "updatedemail@example.com")
    get_user_by_username("testuser")
    delete_user("testuser")
    get_all_users()