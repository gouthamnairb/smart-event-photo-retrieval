from deepface import DeepFace

def get_face_encoding(image_path):
    """
    Extracts facial embeddings using DeepFace.
    Returns None if no face is found.
    """
    try:
        embedding = DeepFace.represent(img_path=image_path, model_name="Facenet", enforce_detection=False)
        return embedding[0]["embedding"] if embedding else None
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def compare_faces(user_encoding, photo_encoding, threshold=0.6):
    """
    Compares two face encodings using DeepFace's cosine similarity.
    Returns True if they match.
    """
    try:
        result = DeepFace.verify(img1_path=user_encoding, img2_path=photo_encoding, model_name="Facenet", enforce_detection=False)
        return result["distance"] < threshold  # Returns True if the distance is below the threshold
    except Exception as e:
        print(f"Error comparing faces: {e}")
        return False
