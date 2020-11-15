from app import app
from flask_sqlalchemy import SQLAlchemy

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{BASE_DIR}\\test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    pass
    # author = db.ForeignKey()


class Tag(db.Model):
    pass
