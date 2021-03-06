import pandas as pd
import pickle
import plotly
import plotly.express as px
import json
from flask import Flask, request, render_template

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
cols = ["District Name", "Market Name", "Variety", "Grade", "Price Date"]


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():
    input_features = [x for x in request.form.values()]
    data = pd.DataFrame([input_features], columns=cols)
    data["Price Date"] = data["Price Date"].astype("datetime64")
    data["year"] = [date.year - 2000 for date in data["Price Date"]]
    data["month"] = [date.month for date in data["Price Date"]]
    data["day of the month"] = [date.day for date in data["Price Date"]]
    data["day of the week"] = [date.weekday() for date in data["Price Date"]]
    data["is_weekend"] = [
        1 if (x == 6 or x == 5) else 0 for x in data["day of the week"]
    ]
    data = data.drop(columns=["Price Date"])
    global district_name
    district_name = data["District Name"][0]
    prediction = model.predict(data)
    prediction = int(prediction[0])
    return render_template(
        "predict.html", pred=f"Predicted Modal Price per Quintal is ₹{prediction}"
    )


if __name__ == "__main__":
    app.run(debug=True)
