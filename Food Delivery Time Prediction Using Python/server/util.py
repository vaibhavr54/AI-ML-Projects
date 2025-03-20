import pickle
import numpy as np
import os

model = None

def load_model():
    """Loads the trained machine learning model from a pickle file."""
    global model
    model_path = os.path.join(os.getcwd(), "artifacts", "food_delivery_model.pkl")

    # Debugging: Print file path
    print(f"🔍 Checking model file at: {repr(model_path)}")  # Use repr() to check for hidden characters

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"❌ Model file not found at: {model_path}")

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    print("✅ Model loaded successfully!")


def predict_delivery_time(age, ratings, distance):
    """Predicts delivery time based on input features."""
    if model is None:
        load_model()
    
    features = np.array([[age, ratings, distance]])
    return model.predict(features)[0]