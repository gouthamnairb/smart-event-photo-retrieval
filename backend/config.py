import os

# Base directory of the project (one level above the backend folder)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Folder where event photos are stored
EVENT_PHOTOS_DIR = os.path.join(BASE_DIR, "event_photos")

# Folder where user-uploaded selfies will be stored temporarily
USER_UPLOADS_DIR = os.path.join(BASE_DIR, "user_uploads")
