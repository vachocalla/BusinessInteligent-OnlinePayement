from flask import request, jsonify
import server
from controller import transaccion_controller

# CREATE
@server.app.route('/transaccions', methods=['POST'])
def transaccion_create():
    return transaccion_controller.transaccion_create()

# READ
@server.app.route('/transaccions/<id>', methods=['GET'])
def transaccion_read(id):
    return transaccion_controller.transaccion_read(id)

# READ
@server.app.route('/transaccions', methods=['GET'])
def transaccions_read():
    return transaccion_controller.transaccions_read()

# UPDATE
@server.app.route('/transaccions/<id>', methods=['PUT','PATCH'])
def transaccion_update(id):
    return transaccion_controller.transaccion_update(id)

# DELETE
@server.app.route('/transaccions/<id>', methods=['DELETE'])
def transaccion_delete(id):
    return transaccion_controller.transaccion_delete(id)

# CREATE
@server.app.route('/transaccions/clientes', methods=['POST'])
def transaccion_cliente_create():
    return transaccion_controller.transaccion_cliente_create()

# READ
@server.app.route('/transaccions/clientes/<id>', methods=['GET'])
def transaccions_cliente_read(id):
    return transaccion_controller.transaccions_cliente_read(id)