import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, String, Float, ForeignKey, BigInteger, Date
from sqlalchemy.orm import relationship
import uuid

def generate_uuid():
    return str(uuid.uuid4())
    
class Producto(db.Base,SerializerMixin):
    __tablename__ = 'producto'
    id = Column(String(256), name="id", primary_key=True, default=generate_uuid)
    nombre = Column(String(256), nullable=True)
    descripcion = Column(String(256), nullable=True)
    sector = Column(String(256), nullable=True)
    precio_unitario = Column(Float)
    #
    empresa_id = Column(String(256), ForeignKey('empresa.id'))
