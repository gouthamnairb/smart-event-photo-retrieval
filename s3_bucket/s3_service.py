import os
from config import s3_client, S3_BUCKET_NAME

def upload_photo_to_s3(file_path, event_name):
    """
    Uploads a photo to S3 inside an event-specific folder.
    """
    file_name = os.path.basename(file_path)
    s3_key = f"{event_name}/{file_name}"
    
    try:
        s3_client.upload_file(file_path, S3_BUCKET_NAME, s3_key)
        photo_url = f"https://{S3_BUCKET_NAME}.s3.amazonaws.com/{s3_key}"
        print(f"Photo uploaded successfully: {photo_url}")
        return photo_url
    except Exception as e:
        print(f"Upload failed: {e}")
        return None

# Test the upload function with a sample file:
if __name__ == "__main__":
    sample_file = "C:/Users/gouth/OneDrive/Desktop/smart-event-photo-retrieval/IMG_1123.jpg"
    upload_photo_to_s3(sample_file, "SampleEvent")
