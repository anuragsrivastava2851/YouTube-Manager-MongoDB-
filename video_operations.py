from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os

# Connect to the database
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["youtube_manager_db"]
videos_collection = db["videos"]


# ---------- CREATE ----------
def create_video(title, channel_id, description, views=0):
    new_video = {
        "title": title,
        "channel_id": channel_id,
        "description": description,
        "views": views,
        "created_at": datetime.now()
    }
    result = videos_collection.insert_one(new_video)
    print("Video created with ID:", result.inserted_id)
    return result.inserted_id


# ---------- READ ----------
def get_all_videos():
    print("\n--- All Videos ---")
    for video in videos_collection.find():
        print(video)


def get_video_by_title(title):
    video = videos_collection.find_one({"title": title})
    if video:
        print("\nVideo found:", video)
    else:
        print("\nNo video found with that title.")
    return video


def get_videos_by_channel(channel_id):
    print(f"\n--- Videos for channel {channel_id} ---")
    for video in videos_collection.find({"channel_id": channel_id}):
        print(video)


# ---------- UPDATE ----------
def update_video_views(title, new_views):
    result = videos_collection.update_one(
        {"title": title},
        {"$set": {"views": new_views}}
    )
    if result.matched_count > 0:
        print(f"\nUpdated {title}'s views to {new_views}")
    else:
        print("\nNo video found to update.")


# ---------- DELETE ----------
def delete_video(title):
    result = videos_collection.delete_one({"title": title})
    if result.deleted_count > 0:
        print(f"\nDeleted video: {title}")
    else:
        print("\nNo video found to delete.")


# ---------- Testing the functions ----------
if __name__ == "__main__":
    get_all_videos()
    create_video("Test Video", "someChannelId", "A test video", 0)
    get_video_by_title("Test Video")
    update_video_views("Test Video", 100)
    get_video_by_title("Test Video")
    delete_video("Test Video")
    get_all_videos()