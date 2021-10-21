import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class Transaccion(db.Base,SerializerMixin):
    __tablename__ = 'transaccion'
    id = Column(String(256), name="id", primary_key=True, default=generate_uuid)
    detalle = Column(String(256), nullable=True)
    monto_transaccion_bs = Column(Float, nullable=True)
    monto_transaccion_usd = Column(Float, nullable=True)

    pasarelapago_id = Column(String(256), ForeignKey('pasarelapago.id'))
    