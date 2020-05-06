from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    """User Model"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String, nullable=False)

    def serialize(self):
        """Serialize a user SQLAlchemy obj to dictionary."""
        # Need serialization bc python can't just turn objects into JSON

        return {
            "name": self.name,
            "email": self.email,
            "year": self.year,
            "color": self.color
        }

    def __repr__(self):
        return f"<User {self.id} name={self.name}, email={self.email}, year={self.year}, color={self.color}>"
