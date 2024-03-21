from flask import Flask
from flask_smorest import Api
from Config import Config


app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

from resources.post import bp as post_bp
app.register_blueprint(post_bp)

from resources.car import bp as car_bp
app.register_blueprint(car_bp)
