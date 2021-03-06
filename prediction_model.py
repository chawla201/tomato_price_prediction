import pandas as pd
import pickle


def load_model():
    model = pickle.load(open("model.pkl", "rb"))
    return model


def predict(model, instance):
    print(model)
    print(instance)
    data = pd.DataFrame(instance)
    data["Price Date"] = data["Price Date"].astype("datetime64")
    data["year"] = [date.year - 2000 for date in data["Price Date"]]
    data["month"] = [date.month for date in data["Price Date"]]
    data["day of the month"] = [date.day for date in data["Price Date"]]
    data["day of the week"] = [date.weekday() for date in data["Price Date"]]
    data["is_weekend"] = [
        1 if (x == 6 or x == 5) else 0 for x in data["day of the week"]
    ]
    data = data.drop(columns=["Price Date"])
    prediction = model.predict(data)
    return prediction[0]