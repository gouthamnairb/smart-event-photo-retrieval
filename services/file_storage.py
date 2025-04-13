import os
import sys

# Get the directory where this script is located
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory (root of the project)
root_dir = os.path.dirname(current_dir)
# Add the root directory to the Python path
sys.path.append(root_dir)

from config import EVENT_PHOTOS_DIR

def list_event_photos():
    """
    Returns a list of full file paths to all image files in the event photos directory.
    """
    photos = []
    for filename in os.listdir(EVENT_PHOTOS_DIR):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            photos.append(os.path.join(EVENT_PHOTOS_DIR, filename))
    return photos
