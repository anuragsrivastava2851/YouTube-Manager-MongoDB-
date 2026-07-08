from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os

# Connect to the database
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["youtube_manager_db"]
comments_collection = db["comments"]


# ---------- CREATE ----------
def create_comment(video_id, user_id, text):
    new_comment = {
        "video_id": video_id,
        "user_id": user_id,
        "text": text,
        "created_at": datetime.now()
    }
    result = comments_collection.insert_one(new_comment)
    print("Comment created with ID:", result.inserted_id)
    return result.inserted_id


# ---------- READ ----------
def get_all_comments():
    print("\n--- All Comments ---")
    for comment in comments_collection.find():
        print(comment)


def get_comments_by_video(video_id):
    print(f"\n--- Comments for video {video_id} ---")
    for comment in comments_collection.find({"video_id": video_id}):
        print(comment)


def get_comments_by_user(user_id):
    print(f"\n--- Comments by user {user_id} ---")
    for comment in comments_collection.find({"user_id": user_id}):
        print(comment)



def update_comment_text(comment_id, new_text):
    result = comments_collection.update_one(
        {"_id": comment_id},
        {"$set": {"text": new_text}}
    )
    if result.matched_count > 0:
        print(f"\nUpdated comment {comment_id}")
    else:
        print("\nNo comment found to update.")



def delete_comment(comment_id):
    result = comments_collection.delete_one({"_id": comment_id})
    if result.deleted_count > 0:
        print(f"\nDeleted comment: {comment_id}")
    else:
        print("\nNo comment found to delete.")



if __name__ == "__main__":
    get_all_comments()
    new_id = create_comment("someVideoId", "someUserId", "This is a test comment")
    get_comments_by_video("someVideoId")
    update_comment_text(new_id, "Updated comment text")