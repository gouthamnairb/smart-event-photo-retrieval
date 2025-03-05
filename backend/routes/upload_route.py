from fastapi import APIRouter, File, UploadFile
import os
import shutil
from backend.config import USER_UPLOADS_DIR
from backend.services.face_recognition import get_face_encoding, compare_faces
from backend.services.file_storage import list_event_photos

router = APIRouter()

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
            matching_photos.append(photo)
    
    return {"matching_photos": matching_photos}
