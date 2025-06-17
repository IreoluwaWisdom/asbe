import onnxruntime as ort
import numpy as np
import cv2

MODEL_PATH = "app/arcfaceresnet100-11-int8.onnx"

# Load the ONNX model
session = ort.InferenceSession(MODEL_PATH)

def preprocess_image(image_path):
    """Load and preprocess the image for ONNX model."""
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (112, 112))  # Resize to model input size
    image = np.transpose(image, (2, 0, 1))  # Change shape to (C, H, W)
    image = image.astype(np.float32) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

def extract_embedding(image_path):
    """Extract facial embedding from image using ONNX model."""
    input_data = preprocess_image(image_path)
    embedding = session.run(None, {"data": input_data})[0]
    return embedding.flatten()  # Convert to 1D vector

def compare_embeddings(embedding1, embedding2, threshold=0.6):
    """Compare two face embeddings using cosine similarity."""
    dot_product = np.dot(embedding1, embedding2)
    norm1 = np.linalg.norm(embedding1)
    norm2 = np.linalg.norm(embedding2)
    similarity = dot_product / (norm1 * norm2)
    return similarity >= threshold

def process_image(image_path):
    """Process image, extract embedding, and compare with stored embeddings."""
    try:
        embedding = extract_embedding(image_path)

        # TODO: Compare against stored embeddings in a database
        # Placeholder: Just return the embedding for now
        return {"message": "Face detected!", "embedding": embedding.tolist()}

    except Exception as e:
        return {"error": str(e)}