from flask import request, jsonify
import server,db
from entity.empresa_entity import Empresa

# CREATE
def empresa_create():
    json = request.json
    empresa = Empresa(**json)
    db.session.add(empresa)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= json
    )

# READ
def empresa_read(id):
    empresa = db.session.query(Empresa).get(id)
    return jsonify( 
        status= "success",
        data= empresa.to_dict()
    )

# READ
def empresas_read():
    empresas = db.session.query(Empresa).all()
    return jsonify( 
        status= "success",
        data= [empresa.to_dict() for empresa in empresas]
    )

# UPDATE
def empresa_update(id):
    json = request.json
    empresa = db.session.query(Empresa).get(id)
    for key, value in json.items():
        if hasattr(empresa, key):
            setattr(empresa, key, value)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= empresa.to_dict()
    )

# DELETE
def empresa_delete(id):
    empresa = db.session.query(Empresa).get(id)
    db.session.delete(empresa)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= empresa.to_dict()
    )

def empresa_cliente_create():
    json = request.json
    empresa = Empresa(**json)
    db.session.add(empresa)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= json
    )

# READ
def empresas_cliente_read(id):
    #empresas = db.session.query(empresa).filter(empresa.cliente==id).all()
    empresas = db.session.query(Empresa).filter(Empresa.cliente_id==id).all()
    return jsonify( 
        status= "success",
        data= [empresa.to_dict() for empresa in empresas]
    )