from prediction_model import load_model, predict
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import os

app = Flask(__name__)
api = Api(app)


class TomatoPricePredictor(Resource):
    def __init__(self):
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument(
            "district", type=str, required=True, help="Please provide district name"
        )
        self.reqparser.add_argument(
            "market", type=str, required=True, help="Please provide market name"
        )
        self.reqparser.add_argument(
            "variety", type=str, required=True, help="Please provide variety"
        )
        self.reqparser.add_argument(
            "grade", type=str, required=True, help="Specify grade"
        )
        self.reqparser.add_argument(
            "date", type=str, required=True, help="Provide price date"
        )

    def post(self):
        args = self.reqparser.parse_args()
        district = args["district"]
        market = args["market"]
        variety = args["variety"]
        grade = args["grade"]
        date = args["date"]

        jsonoutput = {"result": "success"}
        instance = {
            "District Name": [district],
            "Market Name": [market],
            "Variety": [variety],
            "Grade": [grade],
            "Price Date": [date],
        }

        try:
            model = load_model()
            prediction = predict(model, instance)
            jsonoutput["Predicted Price"] = prediction

        except Exception as ex:
            jsonoutput = {"result": "failure", "Exception": str(ex)}

        finally:
            return jsonify(jsonoutput)


api.add_resource(TomatoPricePredictor, "/predict")

if __name__ == "__main__":
    app.run("127.0.0.1", 5014)
