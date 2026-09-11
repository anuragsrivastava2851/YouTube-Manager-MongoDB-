# YouTube Manager (MongoDB)

A command-line application that simulates the core data model of a YouTube-like platform — Users, Channels, Videos, Comments, and Playlists — backed by MongoDB. The project demonstrates full CRUD (Create, Read, Update, Delete) operations across five interlinked collections through a menu-driven CLI.

---

## 📂 Project Structure

```
YouTube-Manager-MongoDB-/
│
├── main.py                    # Entry point — main menu and all sub-menus (User/Channel/Video/Comment/Playlist)
├── connection.py               # MongoDB connection setup
├── user_operations.py          # CRUD operations for Users
├── channel_operations.py       # CRUD operations for Channels
├── video_operations.py         # CRUD operations for Videos
├── comment_operations.py       # CRUD operations for Comments
├── playlist_operations.py      # CRUD operations for Playlists
├── .env                        # Environment variables (MongoDB connection string, etc.)
└── __pycache__/                # Compiled Python cache files
```

---

## ✨ Features

The CLI is organized into five management modules, each accessible from the main menu.

### 👤 User Management
- Create a new user (username, email)
- View all users
- Find a user by username
- Update a user's email
- Delete a user

### 📺 Channel Management
- Create a new channel (name, owner ID, description)
- View all channels
- Find a channel by name
- Update a channel's description
- Delete a channel

### 🎬 Video Management
- Create a new video (title, channel ID, description)
- View all videos
- Find a video by title
- View all videos belonging to a specific channel
- Update a video's view count
- Delete a video

### 💬 Comment Management
- Create a new comment (video ID, user ID, text)
- View all comments
- View comments on a specific video
- View comments made by a specific user
- Delete a comment

### 🎵 Playlist Management
- Create a new playlist (name, user ID)
- View all playlists
- Find a playlist by name
- Add a video to a playlist
- Remove a video from a playlist
- Delete a playlist

---

## 🗂️ Data Model (MongoDB Collections)

| Collection  | Key Fields (inferred from operations)         | Relationships                        |
|-------------|-----------------------------------------------|---------------------------------------|
| `users`     | `username`, `email`                           | Owns channels, playlists; writes comments |
| `channels`  | `name`, `owner_id`, `description`             | Belongs to a user; contains videos    |
| `videos`    | `title`, `channel_id`, `description`, `views` | Belongs to a channel; has comments    |
| `comments`  | `video_id`, `user_id`, `text`                 | Linked to a video and a user          |
| `playlists` | `name`, `user_id`, `videos[]`                 | Belongs to a user; references videos  |

---

## 🛠️ Tech Stack

| Category         | Technology            |
|------------------|-------------------------|
| Language          | Python 3               |
| Database          | MongoDB                |
| DB Driver         | PyMongo                |
| Config Management | `python-dotenv` (`.env`) |
| Interface         | Command-Line Interface (CLI) |

---

## ⚙️ Installation

### Prerequisites
- Python 3.8+
- A MongoDB instance (local or a cloud cluster such as MongoDB Atlas)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/anuragsrivastava2851/YouTube-Manager-MongoDB-.git
   cd YouTube-Manager-MongoDB-
   ```

2. **Install dependencies**
   ```bash
   pip install pymongo python-dotenv
   ```

3. **Configure environment variables**

   Create a `.env` file in the project root with your MongoDB connection details:
   ```env
   MONGO_URI=your_mongodb_connection_string
   DB_NAME=your_database_name
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

---

## 🎯 Usage

On launch, the CLI presents the main menu:

```
===== YOUTUBE MANAGER CLI =====
1. Manage Users
2. Manage Channels
3. Manage Videos
4. Manage Comments
5. Manage Playlists
0. Exit
```

Selecting any option opens that module's sub-menu (e.g. the User menu lets you create, view, find, update, or delete users). Each sub-menu has a `0` option to return to the main menu, and the main menu's `0` option exits the program.

**Example — creating a user:**
```
Choose an option: 1

--- USER MENU ---
1. Create user
2. View all users
3. Find user by username
4. Update user email
5. Delete user
0. Back to main menu
Choose an option: 1
Username: john_doe
Email: john@example.com
```

**Example — adding a video to a playlist:**
```
Choose an option: 5

--- PLAYLIST MENU ---
1. Create playlist
2. View all playlists
3. Find playlist by name
4. Add video to playlist
5. Remove video from playlist
6. Delete playlist
0. Back to main menu
Choose an option: 4
Playlist name: My Favorites
Video ID to add: <video_object_id>
```

---

## ⚠️ Notes

- IDs for related documents (e.g. `owner_id`, `channel_id`, `video_id`, `user_id`) are entered manually as MongoDB `ObjectId` strings — there is no built-in lookup/autocomplete for them.
- Input validation is minimal; invalid choices at any menu prompt display an "Invalid choice, try again." message and re-prompt.
- The `.env` file should never be committed to version control, as it holds database credentials.

---

## 👨‍💻 Author

**Anurag Srivastava**
🔗 [GitHub](https://github.com/anuragsrivastava2851)
📧 anuragsrivastava2851@gmail.com

---

## 📄 License

This project is open-source and available for learning purposes.
