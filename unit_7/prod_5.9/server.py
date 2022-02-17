import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/hello")
def say_hello():
    name = request.args.get("name", "unknown user")
    return f"hello {name}", 200


@app.route("/")
def display_home_page():
    return "hello world"


@app.route("/add", methods=["POST"])
def increase_number():
    number = request.json.get("num", 0)
    if number >= 10:
        return "too much", 400
    return jsonify({"result": number + 1})


if __name__ == "__main__":
    app.run("127.0.0.1", 5000)
