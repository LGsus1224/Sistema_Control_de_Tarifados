from app.libs import db
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

class Area(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_Zona = Column(Integer, ForeignKey('zona.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    parqueadero = Column(Boolean, nullable=False)
    parqueos_no_permitidos = Column(Boolean, nullable=False)
    ocupado = Column(Boolean, nullable=False)
   
    def _init_(self,id_Zona, parquedero,parqueos_no_permitidos, ocupado ):
        self.id_Zona = id_Zona
        self.parqueadero = parquedero
        self.parqueos_no_permitidos = parqueos_no_permitidos
        self.ocupado = ocupado
        super().__init__()