#Sirve para ejecutar la aplicación 

from app import create_app
from app.libs import db


settings_module = 'config.settings' #Variable para cargar los archivos de la ruta de configuración carpeta config. settings


#Función main para ejecutar la aplicación 
if __name__ == '__main__':
    app=create_app(settings_module=settings_module)
    
    #Con el contexto de la aplicación se crean los modelos en la base de datos 
    with app.app_context():
        db.create_all()
    app.run() 
    
    
