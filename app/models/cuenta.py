from app.libs import db, login_manager
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from werkzeug.security import check_password_hash, generate_password_hash

class Cuenta(db.Model, UserMixin) :
    id = Column(Integer, primary_key=True, autoincrement=True)
    rol = Column(String(50), nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(102), nullable=False)

    def __init__(self, rol:str, username:str, password:str):
        self.rol = rol
        self.username = username
        self.password = password
        super().__init__()
    
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password,password)

    @classmethod
    def hash_password(self, password):
        return generate_password_hash(password)

    @login_manager.user_loader
    def load_user(user_id):
        return Cuenta.query.get(user_id)