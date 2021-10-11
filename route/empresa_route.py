from flask import request, jsonify
import server
from controller import empresa_controller

# CREATE
@server.app.route('/empresas', methods=['POST'])
def empresa_create():
    return empresa_controller.empresa_create()

# READ
@server.app.route('/empresas/<id>', methods=['GET'])
def empresa_read(id):
    return empresa_controller.empresa_read(id)

# READ
@server.app.route('/empresas', methods=['GET'])
def empresas_read():
    return empresa_controller.empresas_read()

# UPDATE
@server.app.route('/empresas/<id>', methods=['PUT','PATCH'])
def empresa_update(id):
    return empresa_controller.empresa_update(id)

# DELETE
@server.app.route('/empresas/<id>', methods=['DELETE'])
def empresa_delete(id):
    return empresa_controller.empresa_delete(id)

# CREATE
@server.app.route('/empresas/clientes', methods=['POST'])
def empresa_cliente_create():
    return empresa_controller.empresa_cliente_create()

# READ
@server.app.route('/empresas/clientes/<id>', methods=['GET'])
def empresas_cliente_read(id):
    return empresa_controller.empresas_cliente_read(id)