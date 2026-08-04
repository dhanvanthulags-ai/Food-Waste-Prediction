from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("model/food_waste_model.pkl")

# Load label encoders
label_encoders = joblib.load("model/label_encoders.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get form data
    day = request.form["day"]
    meal = request.form["meal"]
    menu = request.form["menu"]
    students = int(request.form["students"])
    weather = request.form["weather"]
    special_event = request.form["special_event"]
    exam = request.form["exam"]
    food_prepared = int(request.form["food_prepared"])

    # Encode categorical values
    day = label_encoders["DAY"].transform([day])[0]
    meal = label_encoders["MEAL"].transform([meal])[0]
    menu = label_encoders["MENU"].transform([menu])[0]
    weather = label_encoders["WEATHER"].transform([weather])[0]
    special_event = label_encoders["SPECIAL EVENT"].transform([special_event])[0]
    exam = label_encoders["EXAM"].transform([exam])[0]

    # Create input dataframe
    input_data = pd.DataFrame({
        "DAY": [day],
        "MEAL": [meal],
        "MENU": [menu],
        "STUDENTS PRESENT": [students],
        "WEATHER": [weather],
        "SPECIAL EVENT": [special_event],
        "EXAM": [exam],
        "FOOD PREPARED(KG)": [food_prepared]
    })
    input_data.columns = input_data.columns.str.strip()

    print(input_data.columns.tolist())
    # Predict
    prediction = model.predict(input_data)[0]

    return render_template(
        "index.html",
        prediction=round(prediction, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)