from flask import request, jsonify
import server
from controller import cliente_controller

# CREATE
@server.app.route('/clientes', methods=['POST'])
def cliente_create():
    return cliente_controller.cliente_create()

# READ
@server.app.route('/clientes/<id>', methods=['GET'])
def cliente_read(id):
    return cliente_controller.cliente_read(id)

# READ
@server.app.route('/clientes', methods=['GET'])
def clientes_read():
    return cliente_controller.clientes_read()

# UPDATE
@server.app.route('/clientes/<id>', methods=['PUT','PATCH'])
def cliente_update(id):
    return cliente_controller.cliente_update(id)

# DELETE
@server.app.route('/clientes/<id>', methods=['DELETE'])
def cliente_delete(id):
    return cliente_controller.cliente_delete(id)