# Sistema de Control de Tarifados
## Descripción
Sistema web construido en Flask para el control de tarifados en la ciudad de Guaranda

## Preparación e instalación
1. Clonar el repositorio git de [https://github.com/LGsus1224/Sistema_Control_de_Tarifados.git]()
```
git clone https://github.com/LGsus1224/Sistema_Control_de_Tarifados.git
```
2. Crear un entorno virtual en la ruta base
```
python3 -m venv [nombr_ entorno_virtual]
```
o
```
python -m venv [nombr_ entorno_virtual]
```
3. Con el entorno virtual activado instalar los requerimientos del archivo  **requirements.txt**
```
pip install -r requirements.txt
```
4. Crear un archivo .env y asignar las variables de entorno para configurar la aplicación.

### Variables de entorno (.env)
Archivo que contiene las variables de entorno secretas de la aplicación y definen características, keys, accesos y configuraciones para la misma.
La estructura de una variable de entorno es de la siguiente forma:
```
NOMBRE_VARIABLE_DE_ENTORNO = VALOR
```

> Se requiere que este instalada la biblioteca **python-dotenv** que ya se encuentra en el archivo de requerimientos.

> El archivo debe crearse en la ruta base del proyecto.

- **DEBUG** (bool):
    Determina si el servidor se encontrará con el modo debug activado para hotreload.
    > False cuando se encuentre en producción
- **APP_SECRET_KEY** (str):
    Clave secreta de seguridad para firmar sesiones y otros datos sensibles.
- **SQLALCHEMY_DATABASE_URI** (str):
    Dirección de conexión de SQLAlchemy hacia la base de datos. Se define el tipo de gestor de DB, el usuario, contraseña, host y el nombre de la base de datos.
    **Ejemplo:**
    > mysql+pymysql://user:password@host/database_name

## Ejecutar la aplicación (Development)
Ejecutar el comando:
```
python wsgi.py
```
