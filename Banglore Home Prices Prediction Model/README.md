# Real Estate Price Prediction Model

This project is a web-based application that predicts home prices in Bangalore, India, based on various features like location, total square footage, number of bedrooms (BHK), and number of bathrooms. It uses a machine learning model to estimate the price of a house based on user input.

## Features

- **Location-based Price Prediction**: Predict home prices based on the location.
- **Home Details Input**: Input total square footage, number of bedrooms (BHK), and number of bathrooms to get the estimated price.
- **User-Friendly Interface**: A simple and interactive web interface for users to interact with the model.

## Technologies Used

- **Flask**: A lightweight Python web framework to create the web application.
- **Machine Learning**: Linear Regression model for price prediction.
- **HTML/CSS/JS**: For building the user interface.
- **JavaScript**: To handle dynamic content updates.
- **Scikit-Learn**: For implementing the machine learning model.
- **Pandas**: For data manipulation and preprocessing.
- **NumPy**: For numerical operations.

## Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/yourusername/house-price-prediction-bangalore.git
cd house-price-prediction-bangalore
```

### 2. Install dependencies
Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Install the required packages:
```
pip install -r requirements.txt
```

### 3. Run the Flask Application
Start the Flask server to run the application locally:
```
python server.py
```

The application will be available at `http://127.0.0.1:5000/`.

## How the Model Works

- **Type**: Linear Regression, a supervised learning algorithm used for predicting continuous values.
- **Features**: The model uses features such as location, total square footage, number of bedrooms (BHK), and number of bathrooms to predict home prices.
- **Training Data**: The model was trained on real estate data from Bangalore, India.
- **Preprocessing**: Data preprocessing includes handling missing values and encoding categorical variables like location.
- **Prediction**: The trained model predicts the price of a home based on the provided inputs from the user.

## Project Structure

```
house-price-prediction-bangalore/
├── server.py                 # Flask server
├── util.py                   # Helper functions for model loading and prediction
├── server/templates/         # HTML templates for frontend
│   └── app.html              # The main HTML file
├── server/static/            # Static files (CSS, JavaScript, Images)
│   └── app.js                # JavaScript for dynamic content
│   └── app.css               # CSS styles for the UI
├── model/                    # Folder containing model artifacts
│   └── bangalore_home_price_model.pkl   # Trained model file
├── requirements.txt          # List of Python dependencies
└── README.md                 # Project documentation
```
