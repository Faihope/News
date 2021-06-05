from app.config import DevConfig
from flask import Flask

#initializing application
app = Flask(__name__)

#setting up configuration
app.config.from_object(DevConfig)
from app import views