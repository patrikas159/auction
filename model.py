from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.VARCHAR(50))
    username = db.Column(db.VARCHAR(50))
    password = db.Column(db.VARCHAR(50))