from flask import request, jsonify
import server,db
from entity.factura_entity import Factura

# CREATE
def factura_create():
    json = request.json
    factura = Factura(**json)
    db.session.add(factura)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= json
    )

# READ
def factura_read(id):
    factura = db.session.query(Factura).get(id)
    return jsonify( 
        status= "success",
        data= factura.to_dict()
    )

# READ
def facturas_read():
    facturas = db.session.query(Factura).all()
    return jsonify( 
        status= "success",
        data= [factura.to_dict() for factura in facturas]
    )

# UPDATE
def factura_update(id):
    json = request.json
    factura = db.session.query(Factura).get(id)
    for key, value in json.items():
        if hasattr(factura, key):
            setattr(factura, key, value)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= factura.to_dict()
    )

# DELETE
def factura_delete(id):
    factura = db.session.query(Factura).get(id)
    db.session.delete(factura)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= factura.to_dict()
    )

def factura_cliente_create():
    json = request.json
    factura = Factura(**json)
    db.session.add(factura)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= json
    )

# READ
def facturas_cliente_read(id):
    #facturas = db.session.query(Factura).filter(Factura.cliente==id).all()
    facturas = db.session.query(Factura).filter(Factura.cliente_id==id).all()
    return jsonify( 
        status= "success",
        data= [factura.to_dict() for factura in facturas]
    )