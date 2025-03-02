import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import s3_client, S3_BUCKET_NAME

class SyncHandler(FileSystemEventHandler):
    def __init__(self, event_name):
        self.event_name = event_name

    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith((".jpg", ".png", ".jpeg")):
            self.upload_to_s3(event.src_path)

    def on_modified(self, event):
        if not event.is_directory and event.src_path.lower().endswith((".jpg", ".png", ".jpeg")):
            self.upload_to_s3(event.src_path)

    def upload_to_s3(self, local_path):
        file_name = os.path.basename(local_path)
        s3_key = f"{self.event_name}/{file_name}"
        try:
            s3_client.upload_file(local_path, S3_BUCKET_NAME, s3_key)
            print(f"Uploaded {local_path} to s3://{S3_BUCKET_NAME}/{s3_key}")
        except Exception as e:
            print(f"Failed to upload {local_path}: {e}")

def start_sync(local_folder, event_name):
    observer = Observer()
    event_handler = SyncHandler(event_name)
    observer.schedule(event_handler, local_folder, recursive=False)
    observer.start()
    print(f"Monitoring '{local_folder}' for new photos (event: {event_name})...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Stopped monitoring.")
    observer.join()

if __name__ == "__main__":
    # Replace with the local folder you want to monitor
    folder_to_watch = r"C:\Users\gouth\OneDrive\Desktop\smart-event-photo-retrieval\event_photos"
    # Replace with the event folder name to use in S3
    event_folder = "SampleEvent"
    start_sync(folder_to_watch, event_folder)
