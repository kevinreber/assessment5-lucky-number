from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"

BASE_URL = "http://numbersapi.com"


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


@app.route("/api/get-lucky-num", methods=["POST"])
def post_api():
    """Post to API"""

    name = request.json["name"]
    email = request.json["email"]
    year = request.json["year"]
    color = request.json["color"]

    # check for valid inputs and return errors in JSON
    if name == "" or color not in ["red", "green", "orange", "blue"]:
        errors = []
        if name == "":
            name = {"name": "This field is required"}
            errors.append(name)

        if color not in ["red", "green", "orange", "blue"]:
            color = {
                "color": "Invalid color, must be one of: red, green, orange, blue"}
            errors.append(color)

        return (jsonify(errors=errors), 201)

    else:

        random_num_resp = requests.get(url=f"{BASE_URL}/random?json")
        year_resp = requests.get(url=f"{BASE_URL}/{year}?json")

        num_json = random_num_resp.json()
        year_json = year_resp.json()

        # JSON response
        resp_json = {
            "num": {
                "fact": num_json["text"],
                "num": num_json["number"]
            },
            "year": {
                "fact": year_json["text"],
                "year": year_json["number"]
            }
        }

        return (resp_json, 201)
