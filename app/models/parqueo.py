from app.libs import db
from sqlalchemy import Column, String, Integer, ForeignKey,  DateTime

class Parqueo(db.Model):
    placa = Column(String(10), primary_key=True, nullable=False, unique=True)
    id_Area = Column(Integer, ForeignKey("area.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    cedula = Column (String(10), nullable = False)
    codigo = Column (String(6), nullable = False)
    hora = Column (DateTime, nullable = False)

    def _init_(self, placa, id_area, cedula, codigo, hora ):
        self.placa = placa
        self.id_area = id_area
        self.cedula = cedula
        self.codigo = codigo
        self.hora = hora
        super().__init__()