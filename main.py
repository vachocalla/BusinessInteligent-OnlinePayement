"""
pip install SQLAlchemy-serializer
pip install Flask-Seeder
"""
from sqlalchemy import log
import server
import db
import entity.cliente_entity
import entity.empresa_entity
import entity.producto_entity
import entity.pasarelapago_entity
import entity.transaccion_entity
import entity.factura_entity
import entity.detallefactura_entity

import route.cliente_route
import route.empresa_route
import route.producto_route
import route.pasarelapago_route
import route.transaccion_route
import route.factura_route
import route.detallefactura_route

import seed

if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    print("-------------------------------")
    seed.generateDataInit()
    print("-------------------------------")
    #server.app.run(host='0.0.0.0', port='6789', debug=True)
    server.app.run(host='0.0.0.0', port='6789')
    
