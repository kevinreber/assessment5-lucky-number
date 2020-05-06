from flask import Flask, request, redirect, jsonify, render_template
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///lucky-nums-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)
# Build columns
db.create_all()


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
        # Take data from form to make new_user
        new_user = User(
            name=name,
            email=email,
            year=year,
            color=color
        )

        # Add new_user to db
        db.session.add(new_user)
        db.session.commit()

        # Return new_user as json with status code
        new_user_serialized = new_user.serialize()
        resp_json = jsonify(user=new_user_serialized)

        return (resp_json, 201)
