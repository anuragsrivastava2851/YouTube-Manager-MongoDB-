from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os

# Connect to the database
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["youtube_manager_db"]
channels_collection = db["channels"]


# ---------- CREATE ----------
def create_channel(channel_name, owner_id, description):
    new_channel = {
        "channel_name": channel_name,
        "owner_id": owner_id,
        "description": description,
        "created_at": datetime.now()
    }
    result = channels_collection.insert_one(new_channel)
    print("Channel created with ID:", result.inserted_id)
    return result.inserted_id


# ---------- READ ----------
def get_all_channels():
    print("\n--- All Channels ---")
    for channel in channels_collection.find():
        print(channel)


def get_channel_by_name(channel_name):
    channel = channels_collection.find_one({"channel_name": channel_name})
    if channel:
        print("\nChannel found:", channel)
    else:
        print("\nNo channel found with that name.")
    return channel


# ---------- UPDATE ----------
def update_channel_description(channel_name, new_description):
    result = channels_collection.update_one(
        {"channel_name": channel_name},
        {"$set": {"description": new_description}}
    )
    if result.matched_count > 0:
        print(f"\nUpdated {channel_name}'s description")
    else:
        print("\nNo channel found to update.")


# ---------- DELETE ----------
def delete_channel(channel_name):
    result = channels_collection.delete_one({"channel_name": channel_name})
    if result.deleted_count > 0:
        print(f"\nDeleted channel: {channel_name}")
    else:
        print("\nNo channel found to delete.")


# ---------- Testing the functions ----------
if __name__ == "__main__":
    get_all_channels()
    create_channel("Test Channel", "someUserId", "A test channel")
    get_channel_by_name("Test Channel")
    update_channel_description("Test Channel", "Updated description")
    get_channel_by_name("Test Channel")
    delete_channel("Test Channel")
    get_all_channels()