from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the trained machine learning model
model = joblib.load("best_churn_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get data from HTML form
    tenure = float(request.form["tenure"])
    monthly_charges = float(request.form["monthly_charges"])
    total_charges = float(request.form["total_charges"])
    support_calls = float(request.form["support_calls"])

    contract = request.form["contract"]
    payment_method = request.form["payment_method"]
    internet_service = request.form["internet_service"]
    tech_support = request.form["tech_support"]
    online_security = request.form["online_security"]

    # Create the same 12 features used during model training
    features = [[
        tenure,
        monthly_charges,
        total_charges,
        support_calls,

        # Contract
        1 if contract == "One year" else 0,
        1 if contract == "Two year" else 0,

        # Payment method
        1 if payment_method == "Credit" else 0,
        1 if payment_method == "Debit" else 0,
        1 if payment_method == "UPI" else 0,

        # Internet service
        1 if internet_service == "Fiber" else 0,

        # Tech support
        1 if tech_support == "Yes" else 0,

        # Online security
        1 if online_security == "Yes" else 0
    ]]

    # Make prediction
    prediction = model.predict(features)[0]

    # Calculate churn probability
    probability = model.predict_proba(features)[0][1]

    # Convert prediction to text
    if prediction == 1:
        result = "Churn"
    else:
        result = "No Churn"

    probability = round(probability * 100, 2)

    # Send result back to webpage
    return render_template(
        "index.html",
        prediction=result,
        probability=probability
    )


if __name__ == "__main__":
    app.run(debug=True)