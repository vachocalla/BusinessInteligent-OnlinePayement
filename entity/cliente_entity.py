import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, String, Float, DateTime, BigInteger,Date
from sqlalchemy.orm import relationship
from entity.mydatatype import Point
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class Cliente(db.Base,SerializerMixin):
    __tablename__ = 'cliente'
    id = Column(String(256), name="id", primary_key=True, default=generate_uuid)
    nombre = Column(String(256), nullable=True)
    apellido = Column(String(256), nullable=True)
    fecha_nacimiento = Column(String(256), nullable=True)
    fecha_nacimiento_date = Column(Date, nullable=True)
    fecha_nacimiento_milli = Column(BigInteger, nullable=True)
    fecha_nacimiento_dia_semana = Column(Integer, nullable=True)
    fecha_nacimiento_dia_mes = Column(Integer, nullable=True)
    fecha_nacimiento_semana_anio = Column(Integer, nullable=True)
    fecha_nacimiento_mes_anio = Column(Integer, nullable=True)
    fecha_nacimiento_dia_anio = Column(Integer, nullable=True)
    signo = Column(String(20), nullable=True)
    signo_cat = Column(Integer, nullable=True)
    genero = Column(String(20), nullable=True)
    genero_cat = Column(String(20), nullable=True)
    direccion = Column(String(256), nullable=True)
    direccion_lat = Column(Float)
    direccion_lon = Column(Float)
    direccion_geo = Column(Point)
    pais = Column(String(256), nullable=True)
    departamento = Column(String(256), nullable=True)
    municipio = Column(String(256), nullable=True)
    estado_civil = Column(String(20), nullable=True)
    estado_civil_cat = Column(String(20), nullable=True)
    no_hijos = Column(Integer, nullable=True)
    grado_academico = Column(String(256), nullable=True)
    grado_academico_cat = Column(String(30), nullable=True)
