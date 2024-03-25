from flask import Flask
from flask_smorest import Api
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.car_model import CarModel

from resources.post import bp as post_bp
app.register_blueprint(post_bp)
from resources.car import bp as car_bp
app.register_blueprint(car_bp)