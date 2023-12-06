from app.libs import db
from sqlalchemy import Column, Integer, String

class Zona(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    calle_principal = Column(String(100), nullable=False)
    calle_secundaria_1 = Column(String(100), nullable=False)
    calle_secundaria_2 = Column(String(100), nullable=False)
    
    def __init__(self, calle_principal:str, calle_secundaria_1:str, calle_secundaria_2:str):
        self.calle_principal = calle_principal
        self.calle_secundaria_1 = calle_secundaria_1
        self.calle_secundaria_2 = calle_secundaria_2
        super().__init__()