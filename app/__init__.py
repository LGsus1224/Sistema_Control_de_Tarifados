from flask import Flask, redirect, url_for

from app.libs import *
# DB MODELS
from app.models import *


def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(settings_module)

    # Libraries initialization
    db.init_app(app)
    login_manager.init_app(app)

    return app