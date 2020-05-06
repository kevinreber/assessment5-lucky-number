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

    # Take data from form to make new_user
    new_user = User(
        name=request.json["name"],
        email=request.json["email"],
        year=request.json["year"],
        color=request.json["color"]
    )

    # Add new_user to db
    db.add(new_user)
    db.commit()

    # Return new_user as json with status code
    new_user_serialized = new_user.serialize()
    resp_json = jsonify(user=new_user_serialized)

    return (resp_json, 201)
