from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Creating a Flask Application instance to read/apply the config file
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from apps import models


