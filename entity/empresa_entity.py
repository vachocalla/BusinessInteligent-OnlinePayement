import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, String, Float,BigInteger,Date,DateTime
from sqlalchemy.orm import relationship
from entity.mydatatype import Point
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class Empresa(db.Base,SerializerMixin):
    __tablename__ = 'empresa'

    id = Column(String(256), name="id", primary_key=True, default=generate_uuid)
    nombre_fiscal = Column(String(256), nullable=True)
    nombre_comercial = Column(String(256), nullable=True)
    sector = Column(String(256), nullable=True)
    #
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
    direccion = Column(String(256), nullable=True)
    direccion_lat = Column(Float)
    direccion_lon = Column(Float)
    direccion_geo = Column(Point)
    pais = Column(String(256), nullable=True)
    departamento = Column(String(256), nullable=True)
    #
    tamano_empresa = Column(Integer, nullable=True)