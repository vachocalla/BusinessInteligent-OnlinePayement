"""
pip install SQLAlchemy-serializer
"""
import server
import db
import entity.cliente_entity
import entity.factura_entity
import route.cliente_route
import route.factura_route

if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    server.app.run(host='0.0.0.0', port='6789', debug=True)
