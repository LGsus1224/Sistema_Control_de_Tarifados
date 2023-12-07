from flask import Flask
from app.routes import login_bp
from app.libs import *
# DB MODELS
from app.models import *

#Función para instanciar y configurar la aplicación

def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(settings_module)

    # Libraries initialization
    db.init_app(app)
    login_manager.init_app(app)
   
    #Registrar Blueprints de la app
    app.register_blueprint(login_bp)
    return app #Retorna aplicación Flask 
