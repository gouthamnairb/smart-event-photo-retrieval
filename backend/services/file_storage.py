import os
from backend.config import EVENT_PHOTOS_DIR

def list_event_photos():
    """
    Returns a list of full file paths to all image files in the event photos directory.
    """
    photos = []
    for filename in os.listdir(EVENT_PHOTOS_DIR):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            photos.append(os.path.join(EVENT_PHOTOS_DIR, filename))
    return photos
