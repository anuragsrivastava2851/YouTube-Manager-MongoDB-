from user_operations import (
    create_user, get_all_users, get_user_by_username,
    update_user_email, delete_user
)
from channel_operations import (
    create_channel, get_all_channels, get_channel_by_name,
    update_channel_description, delete_channel
)
from video_operations import (
    create_video, get_all_videos, get_video_by_title,
    get_videos_by_channel, update_video_views, delete_video
)
from comment_operations import (
    create_comment, get_all_comments, get_comments_by_video,
    get_comments_by_user, update_comment_text, delete_comment
)
from playlist_operations import (
    create_playlist, get_all_playlists, get_playlist_by_name,
    get_playlists_by_user, add_video_to_playlist,
    remove_video_from_playlist, delete_playlist
)


def user_menu():
    while True:
        print("\n--- USER MENU ---")
        print("1. Create user")
        print("2. View all users")
        print("3. Find user by username")
        print("4. Update user email")
        print("5. Delete user")
        print("0. Back to main menu")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Username: ")
            email = input("Email: ")
            create_user(username, email)
        elif choice == "2":
            get_all_users()
        elif choice == "3":
            username = input("Username to find: ")
            get_user_by_username(username)
        elif choice == "4":
            username = input("Username to update: ")
            new_email = input("New email: ")
            update_user_email(username, new_email)
        elif choice == "5":
            username = input("Username to delete: ")
            delete_user(username)
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")


def channel_menu():
    while True:
        print("\n--- CHANNEL MENU ---")
        print("1. Create channel")
        print("2. View all channels")
        print("3. Find channel by name")
        print("4. Update channel description")
        print("5. Delete channel")
        print("0. Back to main menu")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Channel name: ")
            owner_id = input("Owner ID (user's ObjectId): ")
            description = input("Description: ")
            create_channel(name, owner_id, description)
        elif choice == "2":
            get_all_channels()
        elif choice == "3":
            name = input("Channel name to find: ")
            get_channel_by_name(name)
        elif choice == "4":
            name = input("Channel name to update: ")
            new_description = input("New description: ")
            update_channel_description(name, new_description)
        elif choice == "5":
            name = input("Channel name to delete: ")
            delete_channel(name)
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")


def video_menu():
    while True:
        print("\n--- VIDEO MENU ---")
        print("1. Create video")
        print("2. View all videos")
        print("3. Find video by title")
        print("4. View videos by channel")
        print("5. Update video views")
        print("6. Delete video")
        print("0. Back to main menu")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            channel_id = input("Channel ID: ")
            description = input("Description: ")
            create_video(title, channel_id, description)
        elif choice == "2":
            get_all_videos()
        elif choice == "3":
            title = input("Title to find: ")
            get_video_by_title(title)
        elif choice == "4":
            channel_id = input("Channel ID: ")
            get_videos_by_channel(channel_id)
        elif choice == "5":
            title = input("Title to update: ")
            views = int(input("New view count: "))
            update_video_views(title, views)
        elif choice == "6":
            title = input("Title to delete: ")
            delete_video(title)
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")


def comment_menu():
    while True:
        print("\n--- COMMENT MENU ---")
        print("1. Create comment")
        print("2. View all comments")
        print("3. View comments by video")
        print("4. View comments by user")
        print("5. Delete comment")
        print("0. Back to main menu")
        choice = input("Choose an option: ")

        if choice == "1":
            video_id = input("Video ID: ")
            user_id = input("User ID: ")
            text = input("Comment text: ")
            create_comment(video_id, user_id, text)
        elif choice == "2":
            get_all_comments()
        elif choice == "3":
            video_id = input("Video ID: ")
            get_comments_by_video(video_id)
        elif choice == "4":
            user_id = input("User ID: ")
            get_comments_by_user(user_id)
        elif choice == "5":
            comment_id = input("Comment ID to delete: ")
            delete_comment(comment_id)
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")


def playlist_menu():
    while True:
        print("\n--- PLAYLIST MENU ---")
        print("1. Create playlist")
        print("2. View all playlists")
        print("3. Find playlist by name")
        print("4. Add video to playlist")
        print("5. Remove video from playlist")
        print("6. Delete playlist")
        print("0. Back to main menu")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Playlist name: ")
            user_id = input("User ID: ")
            create_playlist(name, user_id)
        elif choice == "2":
            get_all_playlists()
        elif choice == "3":
            name = input("Playlist name to find: ")
            get_playlist_by_name(name)
        elif choice == "4":
            name = input("Playlist name: ")
            video_id = input("Video ID to add: ")
            add_video_to_playlist(name, video_id)
        elif choice == "5":
            name = input("Playlist name: ")
            video_id = input("Video ID to remove: ")
            remove_video_from_playlist(name, video_id)
        elif choice == "6":
            name = input("Playlist name to delete: ")
            delete_playlist(name)
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")


def main_menu():
    while True:
        print("\n===== YOUTUBE MANAGER CLI =====")
        print("1. Manage Users")
        print("2. Manage Channels")
        print("3. Manage Videos")
        print("4. Manage Comments")
        print("5. Manage Playlists")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            user_menu()
        elif choice == "2":
            channel_menu()
        elif choice == "3":
            video_menu()
        elif choice == "4":
            comment_menu()
        elif choice == "5":
            playlist_menu()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main_menu()