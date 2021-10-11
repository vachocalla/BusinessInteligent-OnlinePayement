import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Producto(db.Base,SerializerMixin):
    __tablename__ = 'factura'
    id = Column(Integer, primary_key=True)
    factura = Column(String(256), nullable=True)
    detalle = Column(String(256), nullable=True)
    valor = Column(Float)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    #cliente = relationship("Cliente", back_populates='facturas')
    #cliente = relationship("Cliente")
    #cliente = relationship("Cliente", back_populates="facturas", cascade_backrefs=False)