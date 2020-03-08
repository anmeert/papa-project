import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine

api = Flask(__name__)
api.config.from_object(Config)
db = SQLAlchemy(api)
migrate = Migrate(api, db)

from api import routes
