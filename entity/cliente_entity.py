import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class Cliente(db.Base,SerializerMixin):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(256), nullable=True)
    descripcion = Column(String(256), nullable=True)
    precio = Column(Float)
    facturas = relationship("Factura")
    #facturas = relationship('Factura', backref='cliente', lazy=True)
    #facturas = relationship("Factura", back_populates="cliente")
    
    """ def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def __repr__(self):
        return f'Producto({self.nombre}, {self.precio})'
    def __str__(self):
        return self.nombre """