from flask import request, jsonify
import server,db
from entity.producto_entity import Producto

# CREATE
def producto_create():
    json = request.json
    producto = Producto(**json)
    db.session.add(producto)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= json
    )

# READ
def producto_read(id):
    producto = db.session.query(Producto).get(id)
    return jsonify( 
        status= "success",
        data= producto.to_dict()
    )

# READ
def productos_read():
    productos = db.session.query(Producto).all()
    return jsonify( 
        status= "success",
        data= [producto.to_dict() for producto in productos]
    )

# UPDATE
def producto_update(id):
    json = request.json
    producto = db.session.query(Producto).get(id)
    for key, value in json.items():
        if hasattr(producto, key):
            setattr(producto, key, value)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= producto.to_dict()
    )

# DELETE
def producto_delete(id):
    producto = db.session.query(Producto).get(id)
    db.session.delete(producto)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= producto.to_dict()
    )

def producto_cliente_create():
    json = request.json
    producto = Producto(**json)
    db.session.add(producto)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= json
    )

# READ
def productos_cliente_read(id):
    #productos = db.session.query(producto).filter(producto.cliente==id).all()
    productos = db.session.query(Producto).filter(Producto.cliente_id==id).all()
    return jsonify( 
        status= "success",
        data= [producto.to_dict() for producto in productos]
    )