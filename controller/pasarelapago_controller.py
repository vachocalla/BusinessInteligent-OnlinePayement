from flask import request, jsonify
import server,db
from entity.pasarelapago_entity import PasarelaPago

# CREATE
def pasarelapago_create():
    json = request.json
    pasarelapago = PasarelaPago(**json)
    db.session.add(pasarelapago)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= json
    )

# READ
def pasarelapago_read(id):
    pasarelapago = db.session.query(PasarelaPago).get(id)
    return jsonify( 
        status= "success",
        data= pasarelapago.to_dict()
    )

# READ
def pasarelapagos_read():
    pasarelapagos = db.session.query(PasarelaPago).all()
    return jsonify( 
        status= "success",
        data= [pasarelapago.to_dict() for pasarelapago in pasarelapagos]
    )

# UPDATE
def pasarelapago_update(id):
    json = request.json
    pasarelapago = db.session.query(PasarelaPago).get(id)
    for key, value in json.items():
        if hasattr(pasarelapago, key):
            setattr(pasarelapago, key, value)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= pasarelapago.to_dict()
    )

# DELETE
def pasarelapago_delete(id):
    pasarelapago = db.session.query(PasarelaPago).get(id)
    db.session.delete(pasarelapago)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= pasarelapago.to_dict()
    )

def pasarelapago_cliente_create():
    json = request.json
    pasarelapago = PasarelaPago(**json)
    db.session.add(pasarelapago)
    db.session.commit()
    return jsonify( 
        status= "success",
        data= json
    )

# READ
def pasarelapagos_cliente_read(id):
    #pasarelapagos = db.session.query(pasarelapago).filter(pasarelapago.cliente==id).all()
    pasarelapagos = db.session.query(PasarelaPago).filter(PasarelaPago.cliente_id==id).all()
    return jsonify( 
        status= "success",
        data= [pasarelapago.to_dict() for pasarelapago in pasarelapagos]
    )