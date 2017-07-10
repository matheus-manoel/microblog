from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Read and use config.py file in root folder
app.config.from_object('config')
# Initialize db
db = SQLAlchemy(app)

from app import views, models
