from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['SECRET KEY'] = 'Secret*23@'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://saccoplus:Today*123@127.0.0.1/saccoplus'


from app import routes