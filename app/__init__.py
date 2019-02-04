from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET KEY'] = 'Secret*23@'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://saccoplus:Today*123@127.0.0.1/saccoplus'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

db.create_all()

u = User(username='john', email='john@example.com')
user1 = User(username='Emma',email='emma@gmail.com')
user2 = User(username='Elvis',email='elvis@gmail.com')
user3 = User(username='Elvin',email='elvin@gmail.com')

db.session.add(u)
db.session.add(user1) 
db.session.add(user2)
db.session.add(user3)

db.session.commit()

from app import routes, models