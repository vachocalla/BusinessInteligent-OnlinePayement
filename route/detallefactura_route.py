from flask import request, jsonify
import server
from controller import detallefactura_controller

# CREATE
@server.app.route('/detallefacturas', methods=['POST'])
def detallefactura_create():
    return detallefactura_controller.detallefactura_create()

# READ
@server.app.route('/detallefacturas/<id>', methods=['GET'])
def detallefactura_read(id):
    return detallefactura_controller.detallefactura_read(id)

# READ
@server.app.route('/detallefacturas', methods=['GET'])
def detallefacturas_read():
    return detallefactura_controller.detallefacturas_read()

# UPDATE
@server.app.route('/detallefacturas/<id>', methods=['PUT','PATCH'])
def detallefactura_update(id):
    return detallefactura_controller.detallefactura_update(id)

# DELETE
@server.app.route('/detallefacturas/<id>', methods=['DELETE'])
def detallefactura_delete(id):
    return detallefactura_controller.detallefactura_delete(id)

# CREATE
@server.app.route('/detallefacturas/clientes', methods=['POST'])
def detallefactura_cliente_create():
    return detallefactura_controller.detallefactura_cliente_create()

# READ
@server.app.route('/detallefacturas/clientes/<id>', methods=['GET'])
def detallefacturas_cliente_read(id):
    return detallefactura_controller.detallefacturas_cliente_read(id)