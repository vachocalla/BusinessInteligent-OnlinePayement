from flask import request, jsonify
import server
from controller import pasarelapago_controller

# CREATE
@server.app.route('/pasarelapagos', methods=['POST'])
def pasarelapago_create():
    return pasarelapago_controller.pasarelapago_create()

# READ
@server.app.route('/pasarelapagos/<id>', methods=['GET'])
def pasarelapago_read(id):
    return pasarelapago_controller.pasarelapago_read(id)

# READ
@server.app.route('/pasarelapagos', methods=['GET'])
def pasarelapagos_read():
    return pasarelapago_controller.pasarelapagos_read()

# UPDATE
@server.app.route('/pasarelapagos/<id>', methods=['PUT','PATCH'])
def pasarelapago_update(id):
    return pasarelapago_controller.pasarelapago_update(id)

# DELETE
@server.app.route('/pasarelapagos/<id>', methods=['DELETE'])
def pasarelapago_delete(id):
    return pasarelapago_controller.pasarelapago_delete(id)

# CREATE
@server.app.route('/pasarelapagos/clientes', methods=['POST'])
def pasarelapago_cliente_create():
    return pasarelapago_controller.pasarelapago_cliente_create()

# READ
@server.app.route('/pasarelapagos/clientes/<id>', methods=['GET'])
def pasarelapagos_cliente_read(id):
    return pasarelapago_controller.pasarelapagos_cliente_read(id)