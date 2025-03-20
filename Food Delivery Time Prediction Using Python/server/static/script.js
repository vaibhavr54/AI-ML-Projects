function predictDeliveryTime(event) {
    if (event) event.preventDefault(); // Prevent form submission (if inside a form)

    let age = parseInt(document.getElementById("age").value);
    let ratings = parseFloat(document.getElementById("ratings").value);
    let distance = parseInt(document.getElementById("distance").value);
    let resultElement = document.getElementById("result");

    // Input validation
    if (isNaN(age) || age < 16) {
        resultElement.innerText = "Error: Age must be at least 16 years old.";
        return;
    }
    if (isNaN(ratings) || ratings < 0 || ratings > 5) {
        resultElement.innerText = "Error: Ratings must be between 0 and 5.";
        return;
    }
    if (isNaN(distance) || distance < 100 || distance > 15000) {
        resultElement.innerText = "Error: Distance must be between 100 and 15000 meters.";
        return;
    }

    // Show loading message before fetching the prediction
    resultElement.innerText = "Calculating...";

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ age: age, ratings: ratings, distance: distance })
    })
    .then(response => response.json())
    .then(data => {
        resultElement.innerText = `Predicted Delivery Time: ${data.predicted_time.toFixed(2)} minutes`;
    })
    .catch(error => {
        console.error("Error:", error);
        resultElement.innerText = "Error predicting time. Please try again.";
    });
}

// Ensure the function is triggered on button click
document.getElementById("predict_button").addEventListener("click", predictDeliveryTime);