from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os


load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["youtube_manager_db"]
playlists_collection = db["playlists"]



def create_playlist(name, user_id, video_ids=None):
    new_playlist = {
        "name": name,
        "user_id": user_id,
        "video_ids": video_ids if video_ids else [],
        "created_at": datetime.now()
    }
    result = playlists_collection.insert_one(new_playlist)
    print("Playlist created with ID:", result.inserted_id)
    return result.inserted_id



def get_all_playlists():
    print("\n--- All Playlists ---")
    for playlist in playlists_collection.find():
        print(playlist)


def get_playlist_by_name(name):
    playlist = playlists_collection.find_one({"name": name})
    if playlist:
        print("\nPlaylist found:", playlist)
    else:
        print("\nNo playlist found with that name.")
    return playlist


def get_playlists_by_user(user_id):
    print(f"\n--- Playlists for user {user_id} ---")
    for playlist in playlists_collection.find({"user_id": user_id}):
        print(playlist)



def add_video_to_playlist(name, video_id):
    result = playlists_collection.update_one(
        {"name": name},
        {"$push": {"video_ids": video_id}}
    )
    if result.matched_count > 0:
        print(f"\nAdded video to playlist: {name}")
    else:
        print("\nNo playlist found to update.")


def remove_video_from_playlist(name, video_id):
    result = playlists_collection.update_one(
        {"name": name},
        {"$pull": {"video_ids": video_id}}
    )
    if result.matched_count > 0:
        print(f"\nRemoved video from playlist: {name}")
    else:
        print("\nNo playlist found to update.")



def delete_playlist(name):
    result = playlists_collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"\nDeleted playlist: {name}")
    else:
        print("\nNo playlist found to delete.")



if __name__ == "__main__":
    get_all_playlists()
    create_playlist("Test Playlist", "someUserId", [])
    add_video_to_playlist("Test Playlist", "someVideoId")
    get_playlist_by_name("Test Playlist")
    remove_video_from_playlist("Test Playlist", "someVideoId")
    delete_playlist("Test Playlist")
    get_all_playlists()