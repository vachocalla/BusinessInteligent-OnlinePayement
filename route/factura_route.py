from flask import request, jsonify
import server
from controller import factura_controller

# CREATE
@server.app.route('/facturas', methods=['POST'])
def factura_create():
    return factura_controller.factura_create()

# READ
@server.app.route('/facturas/<id>', methods=['GET'])
def factura_read(id):
    return factura_controller.factura_read(id)

# READ
@server.app.route('/facturas', methods=['GET'])
def facturas_read():
    return factura_controller.facturas_read()

# UPDATE
@server.app.route('/facturas/<id>', methods=['PUT','PATCH'])
def factura_update(id):
    return factura_controller.factura_update(id)

# DELETE
@server.app.route('/facturas/<id>', methods=['DELETE'])
def factura_delete(id):
    return factura_controller.factura_delete(id)

# CREATE
@server.app.route('/facturas/clientes', methods=['POST'])
def factura_cliente_create():
    return factura_controller.factura_cliente_create()

# READ
@server.app.route('/facturas/clientes/<id>', methods=['GET'])
def facturas_cliente_read(id):
    return factura_controller.facturas_cliente_read(id)