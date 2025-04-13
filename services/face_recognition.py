from deepface import DeepFace
import numpy as np

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
    Compares two face encodings using cosine similarity.
    Returns True if they match (similarity score is above the threshold).
    """
    try:
        # Convert embeddings to numpy arrays if they're not already
        if isinstance(user_encoding, list):
            user_encoding = np.array(user_encoding)
        if isinstance(photo_encoding, list):
            photo_encoding = np.array(photo_encoding)
        
        # Calculate cosine similarity
        dot_product = np.dot(user_encoding, photo_encoding)
        norm_user = np.linalg.norm(user_encoding)
        norm_photo = np.linalg.norm(photo_encoding)
        
        similarity = dot_product / (norm_user * norm_photo)
        
        # Higher similarity means more similar faces
        return similarity > threshold
    except Exception as e:
        print(f"Error comparing faces: {e}")
        return False