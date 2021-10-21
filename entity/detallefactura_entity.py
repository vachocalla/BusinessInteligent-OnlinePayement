import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, BigInteger
from sqlalchemy.orm import relationship
import uuid
from entity.mydatatype import Point

def generate_uuid():
    return str(uuid.uuid4())

class DetalleFactura(db.Base,SerializerMixin):
    __tablename__ = 'detallefactura'
    id = Column(String(256), name="id", primary_key=True, default=generate_uuid)
    fecha = Column(String(256), nullable=True)
    fecha_date = Column(Date, nullable=True)
    fecha_milli = Column(BigInteger, nullable=True)
    fecha_dia_semana = Column(Integer, nullable=True)
    fecha_dia_mes = Column(Integer, nullable=True)
    fecha_semana_anio = Column(Integer, nullable=True)
    fecha_mes_anio = Column(Integer, nullable=True)
    fecha_dia_anio = Column(Integer, nullable=True)
    fecha_anio = Column(Integer, nullable=True)
    #
    producto_nombre = Column(String(256), nullable=True)
    producto_sector = Column(String(256), nullable=True)
    #
    cantidad = Column(Float, nullable=True)
    precio_unitario = Column(Float, nullable=True)
    monto = Column(Float, nullable=True)
    #
    direccion = Column(String(256), nullable=True)
    direccion_lat = Column(Float)
    direccion_lon = Column(Float)
    direccion_geo = Column(Point)
    #
    empresa_nombre = Column(String(256), nullable=True)
    pais = Column(String(256), nullable=True)
    departamento = Column(String(256), nullable=True)
    #
    producto_id = Column(String(256), ForeignKey('producto.id'))
    factura_id = Column(String(256), ForeignKey('factura.id'))
    #