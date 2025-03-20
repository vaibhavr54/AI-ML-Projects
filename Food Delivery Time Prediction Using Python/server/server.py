from flask import Flask, request, jsonify, render_template
import util
import os

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'), static_folder=os.path.join(os.getcwd(), 'static'))

@app.route('/')
def home():
    """Renders the main webpage."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """API endpoint to get the predicted delivery time."""
    data = request.get_json()
    
    age = int(data['age'])
    ratings = float(data['ratings'])
    distance = int(data['distance'])

    estimated_time = util.predict_delivery_time(age, ratings, distance)

    response = {"predicted_time": estimated_time}
    response["predicted_time"] = float(response["predicted_time"][0])  # Extract first value
    return jsonify(response)

if __name__ == "__main__":
    print("Starting Flask Server for Food Delivery Time Prediction...")
    util.load_model()
    app.run(debug=True)