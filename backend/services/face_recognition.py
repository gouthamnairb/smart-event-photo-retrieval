import face_recognition

def get_face_encoding(image_path):
    """
    Loads an image from the given path and returns its face encoding.
    Returns None if no face is found.
    """
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)
    if encodings:
        return encodings[0]
    else:
        return None

def compare_faces(user_encoding, photo_encoding, tolerance=0.6):
    """
    Compares two face encodings. Returns True if they match within the specified tolerance.
    """
    results = face_recognition.compare_faces([user_encoding], photo_encoding, tolerance=tolerance)
    return results[0]
