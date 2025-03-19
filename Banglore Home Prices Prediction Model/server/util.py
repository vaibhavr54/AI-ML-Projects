import pickle
import json
import numpy as np
import os

# Define paths
ARTIFACTS_PATH = os.path.join("server", "artifacts")
COLUMNS_FILE = os.path.join(ARTIFACTS_PATH, "columns.json")
MODEL_FILE = os.path.join(ARTIFACTS_PATH, "banglore_home_prices_model.pickle")

# Global variables
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    """Estimate house price based on input parameters."""
    if __model is None:
        raise ValueError("Model not loaded. Call load_saved_artifacts() first.")

    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        print(f"Warning: Location '{location}' not found in training data.")
        loc_index = -1  # Location not found

    # Create input array
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1  # One-hot encode location

    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    """Load model and column data from artifacts."""
    global __data_columns
    global __locations
    global __model

    print("Loading saved artifacts...")

    # Load columns.json
    try:
        with open(COLUMNS_FILE, "r") as f:
            __data_columns = json.load(f)['data_columns']
            __locations = __data_columns[3:]  # Ignore first 3 columns (sqft, bath, bhk)
    except Exception as e:
        raise FileNotFoundError(f"Error loading {COLUMNS_FILE}: {e}")

    # Load model
    try:
        with open(MODEL_FILE, 'rb') as f:
            __model = pickle.load(f)
    except Exception as e:
        raise FileNotFoundError(f"Error loading {MODEL_FILE}: {e}")

    print("Loading saved artifacts... Done!")

def get_location_names():
    """Return list of locations used in the model."""
    if __locations is None:
        raise ValueError("Data not loaded. Call load_saved_artifacts() first.")
    return __locations

def get_data_columns():
    """Return list of data columns used in the model."""
    if __data_columns is None:
        raise ValueError("Data not loaded. Call load_saved_artifacts() first.")
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print("Available locations:", get_location_names())
    print("Estimated price:", get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print("Estimated price:", get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print("Estimated price:", get_estimated_price('Kalhalli', 1000, 2, 2))  # Unknown location
    print("Estimated price:", get_estimated_price('Ejipura', 1000, 2, 2))   # Unknown location