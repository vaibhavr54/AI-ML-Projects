# MongoDB Query Optimization System with Machine Learning

## Overview

This system predicts MongoDB query execution times and provides suggestions for optimizing query performance based on various metrics such as index usage, the number of documents examined, query length, and more. The machine learning model, trained on query performance data, is integrated into a Python application to help improve query efficiency.

### Key Features:
- **MongoDB Query Execution**: Execute queries on the MongoDB database and sort the results.
- **Machine Learning Predictions**: Use a trained Random Forest Regressor model to predict the execution time of MongoDB queries.
- **Performance Suggestions**: Based on the query's execution characteristics, the system provides actionable suggestions, such as adding indexes or optimizing query structure.
- **Performance Metrics**: Collect important query metrics like query length, index usage, documents examined, and documents returned.

## Requirements

### Python Libraries
- `pymongo`: To interact with MongoDB.
- `joblib`: To load the pre-trained machine learning model and scaler.
- `numpy`: For numerical operations and preparing input data.
- `scikit-learn`: For scaling features and model prediction.
- `time`: To measure query execution time.

Install the required Python libraries using:
```
pip install pymongo joblib numpy scikit-learn
```

### MongoDB
- MongoDB must be installed and running on your system.
- Your database should contain a collection of documents, such as an `orders` collection, for testing.

## How to Use

### 1. Clone the Repository
Clone this repository to your local machine:
```
git clone https://github.com/your-repo/AI Powered Query Optimization.git
```

### 2. Set Up Your MongoDB Database
Ensure MongoDB is running and that you have a database and collection ready. For example, in this project, we assume a collection called `orders`.


### 3. Load Pre-Trained Model
Ensure that your machine learning model and scaler are already trained and saved as `model.pkl` and `scaler.pkl` respectively. If you haven’t trained your model yet, you’ll need to do that before proceeding.

### 4. Update Configuration
In the Python script, update the MongoDB connection details, database, and collection names:
```
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']  # Replace with your database name
collection = db['orders']  # Replace with your collection name
```

### 5. Run the Script
To execute a query, predict its execution time, and get optimization suggestions, run the Python script:
```bash
python your_script_name.py
```

Sample output:
```bash
Predicted execution time: 5.87 ms
Suggestions:
- Consider adding an index to improve query performance.
```

### 6. Customize Queries
You can modify the query to test different scenarios. For example, the following query finds all orders placed by a specific customer and sorts them by `order_date`:
```python
query = {
    "customer_id": "123"  # Replace with an actual customer ID
}
result = collection.find(query).sort("order_date", -1)
```

### 7. Performance Monitoring and Optimization
Based on the suggestions provided, you can:
- **Add Indexes**: Add indexes to improve query performance.
- **Optimize Query Structure**: Refine queries to reduce their complexity and execution time.

Example to create an index:
```javascript
db.orders.createIndex({ customer_id: 1 })
```

## File Structure
```
.
├── model.pkl                 # Pre-trained machine learning model
├── scaler.pkl                # Scaler used for input data
├── your_script_name.py        # Main Python script for executing queries and predictions
└── README.md                 # This readme file
```

## How It Works
1. **Query Execution**: The system first runs a MongoDB query (e.g., filtering and sorting orders by `customer_id` and `order_date`).
2. **Feature Engineering**: Metrics such as query length, index usage, and documents examined are collected.
3. **Prediction**: These features are fed into a machine learning model (Random Forest Regressor) that predicts the query execution time.
4. **Suggestions**: If performance is suboptimal, the system suggests improvements like adding indexes or refining the query.

## Customization
You can modify the system to:
- Add different metrics for feature engineering.
- Train the model on a larger dataset or use a different machine learning algorithm.
- Experiment with different query structures to observe performance changes.
