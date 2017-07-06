from flask import Flask

app = Flask(__name__)
# Read and use config.py file in root folder
app.config.from_object('config')

from app import views
