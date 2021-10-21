import db
import pandas as pd
from faker import Faker
import generate_own_clean,seed_data.datosStatic,seed_data.productos,seed_data.pasarelaPagoData
from faker.providers import internet
from entity.cliente_entity import Cliente
import entity.cliente_entity
from entity.empresa_entity import Empresa
from entity.producto_entity import Producto
from entity.pasarelapago_entity import PasarelaPago
from entity.factura_entity import Factura
from entity.detallefactura_entity import DetalleFactura
from entity.transaccion_entity import Transaccion
import random
import time, datetime
from numpy.random import randint

def generatePasarela():
    dataPasarelas = seed_data.pasarelaPagoData.pasarelas
    faker =Faker()
    for x in range(len(dataPasarelas)):
        print(x)
        dataPasarela = PasarelaPago(
            empresa = dataPasarelas[x][0],
            tipo = dataPasarelas[x][1],
            forma_pago = dataPasarelas[x][2],
        )
        db.session.add(dataPasarela)
    db.session.commit()

if __name__ == "__main__":
    generatePasarela()