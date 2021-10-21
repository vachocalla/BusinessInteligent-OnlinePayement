import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class PasarelaPago(db.Base,SerializerMixin):
    __tablename__ = 'pasarelapago'
    id = Column(String(256), name="id", primary_key=True, default=generate_uuid)
    empresa = Column(String(256), nullable=True)
    tipo = Column(String(20), nullable=True)
    forma_pago = Column(String(20), nullable=True)