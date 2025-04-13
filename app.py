from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
import os
import shutil
from services.face_recognition import get_face_encoding, compare_faces
from services.file_storage import list_event_photos
from config import EVENT_PHOTOS_DIR, USER_UPLOADS_DIR, CORS_ORIGINS, HOST, PORT, DEBUG

# Create the Flask app
app = Flask(__name__)
CORS(app, origins=CORS_ORIGINS)

# Create directories if they don't exist
if not os.path.exists(USER_UPLOADS_DIR):
    os.makedirs(USER_UPLOADS_DIR)
if not os.path.exists(EVENT_PHOTOS_DIR):
    os.makedirs(EVENT_PHOTOS_DIR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/event_photos/<path:filename>')
def serve_event_photo(filename):
    return send_from_directory(EVENT_PHOTOS_DIR, filename)

@app.route('/upload_selfie', methods=['POST'])
def upload_selfie():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Save the uploaded selfie to the user_uploads folder
    upload_path = os.path.join(USER_UPLOADS_DIR, file.filename)
    file.save(upload_path)

    # Compute the face encoding for the uploaded selfie
    user_encoding = get_face_encoding(upload_path)
    if user_encoding is None:
        return jsonify({"error": "No face detected in the uploaded selfie."}), 400

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
    return jsonify(response)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
