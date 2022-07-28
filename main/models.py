import db
from sqlalchemy import Column, Integer, String, Boolean


class Tarea(db.Base):
    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True) # Automaticamente esta PK se convertirá en SERIAL (AUTOINCREMENT)
    contenido = Column(String(200), nullable=False)
    hecha = Column(Boolean)
    comentario = Column(String(200), nullable=True)
    fecha = Column(String(20), nullable=True)

    def __init__(self, contenido, hecha, comentario= "",fecha=""):
        self.contenido = contenido
        self.hecha = hecha
        self.comentario = comentario
        self.fecha = fecha

    def __str__(self):
        return "Tarea({}: {}, {})".format(self.id, self.contenido, self.hecha)

