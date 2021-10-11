from flask import request, jsonify
import server,db
from entity.transaccion_entity import Transaccion

# CREATE
def transaccion_create():
    json = request.json
    transaccion = Transaccion(**json)
    db.session.add(transaccion)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= json
    )

# READ
def transaccion_read(id):
    transaccion = db.session.query(Transaccion).get(id)
    return jsonify( 
        status= "success",
        data= transaccion.to_dict()
    )

# READ
def transaccions_read():
    transaccions = db.session.query(Transaccion).all()
    return jsonify( 
        status= "success",
        data= [transaccion.to_dict() for transaccion in transaccions]
    )

# UPDATE
def transaccion_update(id):
    json = request.json
    transaccion = db.session.query(Transaccion).get(id)
    for key, value in json.items():
        if hasattr(transaccion, key):
            setattr(transaccion, key, value)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= transaccion.to_dict()
    )

# DELETE
def transaccion_delete(id):
    transaccion = db.session.query(Transaccion).get(id)
    db.session.delete(transaccion)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= transaccion.to_dict()
    )

def transaccion_cliente_create():
    json = request.json
    transaccion = Transaccion(**json)
    db.session.add(transaccion)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= json
    )

# READ
def transaccions_cliente_read(id):
    #transaccions = db.session.query(transaccion).filter(transaccion.cliente==id).all()
    transaccions = db.session.query(Transaccion).filter(Transaccion.cliente_id==id).all()
    return jsonify( 
        status= "success",
        data= [transaccion.to_dict() for transaccion in transaccions]
    )