import db
import pandas as pd
from faker import Faker
import generate_own_clean,seed_data.datosStatic,seed_data.productos
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

def generateEmpresa():
    print("-----------------------------------1")
    dfEmpresas = pd.read_csv('data/empresas.csv',index_col=0, encoding='latin-1')
    faker =Faker()
    for x in range(dfEmpresas.shape[0]):
    #for x in range(1):
        print(x)
        fn = generate_own_clean.generate_date_birthday([("1/1/1970", "31/12/1985",0.20),("1/1/1986", "31/12/2008",1.5)])
        fnDate = datetime.datetime.strptime(fn, '%d/%m/%Y')
        if( pd.isna(dfEmpresas.iloc[ x ]['departamento']) ):
            randLugar = generate_own_clean.generarLugar()
        else:
            randLugar = generate_own_clean.generarLugarDepartamento(dfEmpresas.iloc[ x ]['departamento'])

        if( pd.isna(dfEmpresas.iloc[ x ]['direccion']) ):
            randDireccion = faker.address()
        else:
            randDireccion = dfEmpresas.iloc[ x ]['direccion']
        dataEmpresa = Empresa(
            id = entity.cliente_entity.generate_uuid(),
            nombre_fiscal = dfEmpresas.iloc[ x ]['nombre'],
            nombre_comercial = dfEmpresas.iloc[ x ]['nombre'],
            sector = dfEmpresas.iloc[ x ]['sector'].strip().lower(),
            fecha = fn, 
            fecha_date = fnDate,
            fecha_milli = generate_own_clean.to_milliseconds(fnDate),
            fecha_dia_semana = fnDate.weekday(),
            fecha_dia_mes = fnDate.strftime("%d"),
            fecha_semana_anio = fnDate.strftime("%V"),
            fecha_mes_anio = fnDate.strftime("%m"),
            fecha_dia_anio = fnDate.timetuple().tm_yday,
            direccion = randDireccion, 
            direccion_lat = randLugar[1],
            direccion_lon = randLugar[2],
            direccion_geo = 'POINT('+str(randLugar[1])+' '+str(randLugar[2])+')',
            pais = "Bolivia",
            departamento = randLugar[0],
            tamano_empresa = generate_own_clean.generarTamanoEmpresa(),
        )
        db.session.add(dataEmpresa)
        db.session.commit()
        
        dataSectorProducto = seed_data.productos.productosSector
        i=0
        encontrado = False
        while( i<len(dataSectorProducto) ):
            if dataEmpresa.sector.strip().lower()==dataSectorProducto[i]['sector'].strip().lower():
                encontrado = True
                j=0
                while( j<len( dataSectorProducto[i]['productos'] ) ):
                    dataProducto = Producto(
                        nombre = dataSectorProducto[i]['productos'][j][0] ,
                        descripcion = dataSectorProducto[i]['productos'][j][0]+' '+dataSectorProducto[i]['productos'][j][0],
                        sector = dataEmpresa.sector,
                        precio_unitario = dataSectorProducto[i]['productos'][j][1],
                        empresa_id = dataEmpresa.id,
                    )
                    db.session.add(dataProducto)
                    j=j+1
                db.session.commit()
                break
            i=i+1
        if encontrado==False :
            print("No se encontro")

""" if __name__ == "__main__":
    generateEmpresa() """