import db
import pandas as pd
from faker import Faker
import seed_cliente,seed_empresa,seed_pasarela
import generate_own_clean
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

def generateDataInit():
    seed_cliente.generateCliente()
    seed_empresa.generateEmpresa()
    seed_pasarela.generatePasarela()
    compra()
    pass

def compra():
    dfTiempo = pd.read_excel('data/porcentajeCompraProductoGestion.xlsx')
    clientes = db.session.query(Cliente).all()
    pasarelaPagosOnline = db.session.query(PasarelaPago).filter_by(tipo='Pago Online' ).all()
    pasarelaPagosEfectivo = db.session.query(PasarelaPago).filter_by(tipo='Efectivo' ).all()
    probPasarela = pd.read_excel('data/probPasarela.xlsx')

    fi = generate_own_clean.generate_date_birthday([("1/1/2018", "30/1/2018",1.5)])
    fnDate = datetime.datetime.strptime(fi, '%d/%m/%Y')
    longitudSector = dfTiempo.iloc[ 0 ]['tt']-1
    i = 1
    loop = True
    while loop:
        fnDate = fnDate + datetime.timedelta(hours=+8)
        
        if fnDate.time()>=datetime.time(6,00) and fnDate.time()<=datetime.time(22,00):
            newRango = random.randint(1, 10)
        else:
            newRango = random.randint(1, 2)

        randSectors = []
        for jj in range( newRango ):
            rrand = random.random()
            ii=0
            while ii<longitudSector:
                if rrand < dfTiempo.iloc[ ii ]['a'+str(fnDate.year)+'']:
                    randSectors.append( dfTiempo.iloc[ ii ]['sector'].strip().lower() )
                    break
                ii = ii +1
        
        for sector in randSectors:
            empresas = db.session.query(Empresa).filter_by(sector=sector ).all()

            randCliente = random.randint(0, len(clientes)-1)
            randEmpresa = random.randint(0, len(empresas)-1)

            if random.random()<=probPasarela.iloc[ 0 ]['c'+str(fnDate.year)+'']:
                randPasarelapago = random.randint(0, len(pasarelaPagosOnline)-1)
                pasarelaPago = pasarelaPagosOnline[randPasarelapago]
            else:
                randPasarelapago = random.randint(0, len(pasarelaPagosEfectivo)-1)
                pasarelaPago = pasarelaPagosEfectivo[randPasarelapago]
            ## rand pasarela
            dataF = Factura(
                id = entity.cliente_entity.generate_uuid(),
                no = entity.cliente_entity.generate_uuid()+'',
                monto_total = 0,
                fecha = fnDate.strftime("%d/%m/%Y"),
                fecha_date = fnDate,
                fecha_milli = generate_own_clean.to_milliseconds(fnDate),
                fecha_dia_semana = fnDate.weekday(),
                fecha_dia_mes = fnDate.strftime("%d"),
                fecha_semana_anio = fnDate.strftime("%V"),
                fecha_mes_anio = fnDate.strftime("%m"),
                fecha_dia_anio = fnDate.timetuple().tm_yday,
                fecha_anio = fnDate.year,

                cliente_id = clientes[randCliente].id,
                empresa_id = empresas[randEmpresa].id,
                pasarelapago_id = pasarelaPago.id,
            )

            sum = 0
            dataDFs = []
            productos = db.session.query(Producto).filter_by(empresa_id=empresas[randEmpresa].id ).all()
            randIdProductos = randint(0, len(productos), random.randint(1, 20) )
            for prod in randIdProductos:
                dataDF = DetalleFactura (
                    id = entity.cliente_entity.generate_uuid(),

                    fecha = fnDate.strftime("%d/%m/%Y"), 
                    fecha_date = fnDate,
                    fecha_milli = generate_own_clean.to_milliseconds(fnDate),
                    fecha_dia_semana = fnDate.weekday(),
                    fecha_dia_mes = fnDate.strftime("%d"),
                    fecha_semana_anio = fnDate.strftime("%V"),
                    fecha_mes_anio = fnDate.strftime("%m"),
                    fecha_dia_anio = fnDate.timetuple().tm_yday,
                    fecha_anio = fnDate.year,

                    producto_nombre = productos[prod].nombre,
                    producto_sector = productos[prod].sector,

                    cantidad = random.randint(1, 20),
                    precio_unitario = productos[prod].precio_unitario,
                    monto = 0,

                    direccion = empresas[randEmpresa].direccion,
                    direccion_lat = empresas[randEmpresa].direccion_lat,
                    direccion_lon = empresas[randEmpresa].direccion_lon,
                    direccion_geo = empresas[randEmpresa].direccion_geo,

                    empresa_nombre = empresas[randEmpresa].nombre_fiscal,
                    pais = empresas[randEmpresa].pais,
                    departamento = empresas[randEmpresa].departamento,

                    producto_id = productos[prod].id,
                    factura_id = dataF.id,
                )
                dataDF.monto = dataDF.precio_unitario * dataDF.cantidad
                sum = sum + (productos[prod].precio_unitario * dataDF.cantidad)
                dataDFs.append(dataDF)

            dataF.monto_total = sum
            db.session.add(dataF)
            db.session.commit()

            for x in dataDFs:
                db.session.add(x)
                db.session.commit()

        if fnDate>datetime.datetime.now():
            loop = False
        
        i = i + 1

if __name__ == "__main__":
    generateDataInit()



""" fi = generate_own_clean.generate_date_birthday([("1/1/2008", "30/1/2008",1.5)])
    #tiempo = 200
    #fi = generate_own_clean.generate_date_birthday([("1/1/2008", "30/1/2008",1.5)])
    fnDate = datetime.datetime.strptime(fi, '%d/%m/%Y')
    i = 1
    loop = True
    while loop:
        #use_date = use_date + datetime.timedelta(minutes=+10)
        #use_date = use_date + datetime.timedelta(hours=+1)
        #use_date = use_date + datetime.timedelta(days=+1)
        #use_date = use_date + datetime.timedelta(weeks=+1) 
        fnDate = fnDate + datetime.timedelta(hours=+8)
        #print( fnDate, fnDate.strftime("%d/%m/%Y"), datetime.datetime.now())
        if fnDate>datetime.datetime.now():
            loop = False
            print("finish")
        else:
            print("sigue")
        print(i)
        i = i + 1
 """