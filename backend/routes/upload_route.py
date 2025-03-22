from fastapi import APIRouter, File, UploadFile
import os
import shutil
import numpy as np
from backend.config import USER_UPLOADS_DIR, EVENT_PHOTOS_DIR
from backend.services.face_recognition import get_face_encoding, compare_faces
from backend.services.file_storage import list_event_photos

router = APIRouter()

# Create USER_UPLOADS_DIR if it doesn't exist
if not os.path.exists(USER_UPLOADS_DIR):
    os.makedirs(USER_UPLOADS_DIR)

@router.post("/upload_selfie")
async def upload_selfie(file: UploadFile = File(...)):
    # Save the uploaded selfie to the user_uploads folder
    upload_path = os.path.join(USER_UPLOADS_DIR, file.filename)
    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Compute the face encoding for the uploaded selfie
    user_encoding = get_face_encoding(upload_path)
    if user_encoding is None:
        return {"error": "No face detected in the uploaded selfie."}

    # List all event photos from local storage
    event_photos = list_event_photos()
    matching_photos = []

    # Compare the selfie face encoding with each event photo's encoding
    for photo in event_photos:
        photo_encoding = get_face_encoding(photo)
        if photo_encoding is None:
            continue  # Skip photos with no detectable face
        
        if compare_faces(user_encoding, photo_encoding):
            # Append the path relative to the event_photos directory
            relative_path = os.path.relpath(photo, start=EVENT_PHOTOS_DIR)
            relative_path = relative_path.replace("\\", "/")  # Convert Windows paths to URL format
            matching_photos.append(relative_path)

    response = {"matching_photos": matching_photos}
    print("Response to be sent:", response)  # Log the response
    return response