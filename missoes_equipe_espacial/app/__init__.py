from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from app.model.missao import Missao

app = Flask(__name__)
db = SQLAlchemy(app)
CORS(app)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context:
    db.create_all()

