from flask import request, jsonify
import server,db
from entity.cliente_entity import Cliente

# CREATE
def cliente_create():
    json = request.json
    cliente = Cliente(**json)
    db.session.add(cliente)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= json
    )

# READ
def cliente_read(id):
    cliente = db.session.query(Cliente).get(id)
    return jsonify( 
        status= "success",
        data= cliente.to_dict()
    )

# READ
def clientes_read():
    clientes = db.session.query(Cliente).all()
    return jsonify( 
        status= "success",
        data= [cliente.to_dict() for cliente in clientes]
    )

# UPDATE
def cliente_update(id):
    json = request.json
    cliente = db.session.query(Cliente).get(id)
    for key, value in json.items():
        if hasattr(cliente, key):
            setattr(cliente, key, value)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= cliente.to_dict()
    )

# DELETE
def cliente_delete(id):
    cliente = db.session.query(Cliente).get(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= cliente.to_dict()
    )
