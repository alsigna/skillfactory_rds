import json
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    with open("./hw1.pkl", "rb") as pkl_file:
        regressor = pickle.load(pkl_file)

    numbers = request.json
    y_pred = regressor.predict([numbers])
    return jsonify({"prediction": y_pred[0]})


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
