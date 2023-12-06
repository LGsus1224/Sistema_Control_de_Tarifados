from app.libs import db
from sqlalchemy import Column, String,  DateTime

class Retenciones(db.Model):
    _tablename_ = "retenciones"
    id = Column (String(6), primary_key=True)
    placa = Column (String (10))
    codigo=Column (String(10))
    hora= Column (DateTime)
   
    def _init_(self,placa,codigo,hora):
        self.placa=placa
        self.codigo=codigo
        self.codigo=hora
        super().__init__()