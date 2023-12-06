from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = os.getenv('DEBUG')
SECRET_KEY = os.getenv("APP_SECRET_KEY")
# SQLALCHEMY CONFIGURATION
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
