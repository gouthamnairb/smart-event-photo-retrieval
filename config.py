import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Folder where event photos are stored
EVENT_PHOTOS_DIR = os.path.join(BASE_DIR, "event_photos")

# Folder where user-uploaded selfies will be stored temporarily
USER_UPLOADS_DIR = os.path.join(BASE_DIR, "user_uploads")

# CORS allowed origins
CORS_ORIGINS = ["http://127.0.0.1:5501"]

# Flask server settings
HOST = "0.0.0.0"
PORT = 8000
DEBUG = True 