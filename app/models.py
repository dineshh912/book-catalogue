from enum import unique
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db
from app import login
from marshmallow import Schema, fields

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"{self.email}"
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    book_id = db.Column(db.String)
    book_title = db.Column(db.String)
    book_thumb = db.Column(db.String)
    book_author = db.Column(db.String)
    book_page = db.Column(db.Integer)
    book_rating = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.id}"

class BookSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    book_id = fields.Str()
    book_title = fields.Str()
    book_thumb = fields.Str()
    book_author = fields.Str()
    book_page = fields.Int()
    book_rating = fields.Int()

books_schema = BookSchema(many=True)