
# **🍽️ Food Delivery Time Prediction**  

A **Flask-based web application** that predicts the estimated delivery time for food orders using **Machine Learning**. The system takes in user inputs like **age of the delivery partner, ratings of previous deliveries, and total delivery distance** to provide an accurate prediction.  

---

## **🛠️ Tech Stack Used**  

### **Backend**  
- **Flask** – Lightweight Python web framework  
- **scikit-learn** – Machine Learning model for prediction  
- **pandas & NumPy** – Data processing  
- **pickle** – Model serialization (`model.pkl`)  

### **Frontend**  
- **HTML, CSS** – User interface  
- **JavaScript (Vanilla)** – Form validation and API calls  

---

## **🚀 Features**  

✔ **ML-based Prediction:** Uses a trained model to estimate food delivery time  
✔ **Real-time User Input Handling:** Inputs age, ratings, and distance for prediction  
✔ **Input Validation:** Ensures valid inputs for accurate predictions  
✔ **Interactive UI:** Simple, clean, and responsive frontend  
✔ **Flask API Endpoint:** Accepts user inputs and returns predicted time  

---

## **🔧 How to Set Up & Run Locally**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/YOUR_USERNAME/food-delivery-time-prediction.git  
cd food-delivery-time-prediction
```

### **2️⃣ Install Dependencies**  
Ensure you have Python installed, then run:  
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Flask App**  
```sh
python app.py
```
The app will be available at **`http://127.0.0.1:5000/`**.

---

## **📌 API Endpoint**  

### **POST `/predict`**  
Takes **JSON input** and returns the predicted delivery time.  

#### **Request Example:**  
```json
{
  "age": 25,
  "ratings": 4.5,
  "distance": 3000
}
```

#### **Response Example:**  
```json
{
  "predicted_time": 27.48
}
```
