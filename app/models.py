from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    gender = db.column(db.String(120))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(64), index=True, unique=True)
    permissions = db.Column(db.String(120), index=True, unique=True)
   

    def __repr__(self):
        return '<Role {}>'.format(self.role)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)