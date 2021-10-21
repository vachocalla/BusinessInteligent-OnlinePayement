import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime,Date,BigInteger
from sqlalchemy.orm import relationship
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class Factura(db.Base,SerializerMixin):
    __tablename__ = 'factura'
    id = Column(String(256), name="id", primary_key=True, default=generate_uuid)
    no = Column(String(256), nullable=True)
    monto_total = Column(Float, nullable=True)
    fecha = Column(String(256), nullable=True)
    fecha_date = Column(DateTime, nullable=True)
    fecha_milli = Column(BigInteger, nullable=True)
    fecha_dia_semana = Column(Integer, nullable=True)
    fecha_dia_mes = Column(Integer, nullable=True)
    fecha_semana_anio = Column(Integer, nullable=True)
    fecha_mes_anio = Column(Integer, nullable=True)
    fecha_dia_anio = Column(Integer, nullable=True)
    fecha_anio = Column(Integer, nullable=True)
    #
    cliente_id = Column(String(256), ForeignKey('cliente.id'))
    empresa_id = Column(String(256), ForeignKey('empresa.id'))
    pasarelapago_id = Column(String(256), ForeignKey('pasarelapago.id'))
    #