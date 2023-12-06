from app.libs import db
from flask_login import UserMixin
from sqlalchemy import Column, String, Integer, ForeignKey
from werkzeug.security import check_password_hash, generate_password_hash

class Funcionario(db.Model, UserMixin):
    cedula = Column(String(10), primary_key=True)
    id_Cuenta = Column(Integer, ForeignKey('cuenta.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    telefono = Column(String(10), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    
    def __init__(self, cedula:str, id_Cuenta:str, nombre:str,
                apellido:str, telefono:str, email:str, password:str):
        self.cedula = cedula
        self.id_Cuenta = id_Cuenta
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.password = password
        super().__init__()
        
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password,password)

    @classmethod
    def hash_password(self, password):
        return generate_password_hash(password)