from flask import Flask

app = Flask(__name__)

from resources.car import routes
from resources.post import routes