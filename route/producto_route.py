from flask import request, jsonify
import server
from controller import producto_controller

# CREATE
@server.app.route('/productos', methods=['POST'])
def producto_create():
    return producto_controller.producto_create()

# READ
@server.app.route('/productos/<id>', methods=['GET'])
def producto_read(id):
    return producto_controller.producto_read(id)

# READ
@server.app.route('/productos', methods=['GET'])
def productos_read():
    return producto_controller.productos_read()

# UPDATE
@server.app.route('/productos/<id>', methods=['PUT','PATCH'])
def producto_update(id):
    return producto_controller.producto_update(id)

# DELETE
@server.app.route('/productos/<id>', methods=['DELETE'])
def producto_delete(id):
    return producto_controller.producto_delete(id)

# CREATE
@server.app.route('/productos/clientes', methods=['POST'])
def producto_cliente_create():
    return producto_controller.producto_cliente_create()

# READ
@server.app.route('/productos/clientes/<id>', methods=['GET'])
def productos_cliente_read(id):
    return producto_controller.productos_cliente_read(id)