from flask import request, jsonify
import server,db
from entity.detallefactura_entity import DetalleFactura

# CREATE
def detallefactura_create():
    json = request.json
    detallefactura = DetalleFactura(**json)
    db.session.add(detallefactura)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= json
    )

# READ
def detallefactura_read(id):
    detallefactura = db.session.query(DetalleFactura).get(id)
    return jsonify( 
        status= "success",
        data= detallefactura.to_dict()
    )

# READ
def detallefacturas_read():
    detallefacturas = db.session.query(DetalleFactura).all()
    return jsonify( 
        status= "success",
        data= [detallefactura.to_dict() for detallefactura in detallefacturas]
    )

# UPDATE
def detallefactura_update(id):
    json = request.json
    detallefactura = db.session.query(DetalleFactura).get(id)
    for key, value in json.items():
        if hasattr(detallefactura, key):
            setattr(detallefactura, key, value)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= detallefactura.to_dict()
    )

# DELETE
def detallefactura_delete(id):
    detallefactura = db.session.query(DetalleFactura).get(id)
    db.session.delete(detallefactura)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= detallefactura.to_dict()
    )

def detallefactura_cliente_create():
    json = request.json
    detallefactura = DetalleFactura(**json)
    db.session.add(detallefactura)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= json
    )

# READ
def detallefacturas_cliente_read(id):
    #detallefacturas = db.session.query(detallefactura).filter(detallefactura.cliente==id).all()
    detallefacturas = db.session.query(DetalleFactura).filter(DetalleFactura.cliente_id==id).all()
    return jsonify( 
        status= "success",
        data= [detallefactura.to_dict() for detallefactura in detallefacturas]
    )