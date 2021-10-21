import db
import pandas as pd
from faker import Faker
import generate_own_clean,seed_data.datosStatic
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

def generateCliente():
    dfApellidos = pd.read_csv('data/apellidos.csv')
    dfHombres = pd.read_csv('data/hombres.csv')
    dfMujeres = pd.read_csv('data/mujeres.csv')
    print(dfHombres.shape)
    print(dfMujeres.shape)
    #start = time.time()
    faker =Faker()
    for x in range(5000):
        #print("x")
        fn = generate_own_clean.generate_date_birthday([("1/1/1970", "31/12/1985",0.33),("1/1/1986", "31/12/2010",1.5)])
        fnDate = datetime.datetime.strptime(fn, '%d/%m/%Y')
        zodiac = generate_own_clean.programZodiac(fnDate)
        randGenero = generate_own_clean.generarGenero()
        randLugar = generate_own_clean.generarLugar()
        randEC = generate_own_clean.generarEC(fnDate)
        randGa = generate_own_clean.generarGradoAcademico(fn)
        if randGenero[1]=='M':
            randxxx= random.randint(0, dfHombres.shape[0]-1)
            randNombre = dfHombres.iloc[ randxxx ]['nombre']
        else: 
            randxxx= random.randint(0, dfMujeres.shape[0]-1)
            randNombre = dfMujeres.iloc[ randxxx ]['nombre']
        data = Cliente(
            nombre = randNombre,
            apellido = dfApellidos.iloc[ random.randint(0, dfApellidos.shape[0]-1) ]['apellido'],
            fecha_nacimiento = fn, 
            fecha_nacimiento_date = fnDate,
            fecha_nacimiento_milli = generate_own_clean.to_milliseconds(fnDate),
            fecha_nacimiento_dia_semana = fnDate.weekday(),
            fecha_nacimiento_dia_mes = fnDate.strftime("%d"),
            fecha_nacimiento_semana_anio = fnDate.strftime("%V"),
            fecha_nacimiento_mes_anio = fnDate.strftime("%m"),
            fecha_nacimiento_dia_anio = fnDate.timetuple().tm_yday,
            signo = zodiac[0],
            signo_cat = zodiac[1],
            genero = randGenero[0], 
            genero_cat = randGenero[1],
            direccion = faker.address(), 
            direccion_lat = randLugar[1],
            direccion_lon = randLugar[2],
            direccion_geo = 'POINT('+str(randLugar[1])+' '+str(randLugar[2])+')',
            pais = "Bolivia",
            departamento = randLugar[0],
            municipio = "", 
            estado_civil = randEC[0],
            estado_civil_cat = randEC[1],
            no_hijos = randEC[2],
            grado_academico = randGa[0],
            grado_academico_cat = randGa[1]
        )
        if pd.isna(data.nombre):
            print(randxxx)
            print(data.genero)
            print("pd.isna(data.nombre)")
            break
        if pd.isna(data.apellido):
            print("pd.isna(data.apellido)")
            break
        if pd.isna(data.fecha_nacimiento):
            print("pd.isna(data.fecha_nacimiento)")
            break
        if pd.isna(data.fecha_nacimiento_date):
            print("pd.isna(data.fecha_nacimiento_date)")
            break
        if pd.isna(data.fecha_nacimiento_milli):
            print("pd.isna(data.fecha_nacimiento_milli)")
            break
        if pd.isna(data.fecha_nacimiento_dia_semana):
            print("pd.isna(data.fecha_nacimiento_dia_semana)")
            break
        if pd.isna(data.fecha_nacimiento_dia_mes):
            print("pd.isna(data.fecha_nacimiento_dia_mes)")
            break
        if pd.isna(data.fecha_nacimiento_semana_anio):
            print("pd.isna(data.fecha_nacimiento_semana_anio)")
            break
        if pd.isna(data.fecha_nacimiento_mes_anio):
            print("pd.isna(data.fecha_nacimiento_mes_anio)")
            break
        if pd.isna(data.fecha_nacimiento_dia_anio):
            print("pd.isna(data.fecha_nacimiento_dia_anio)")
            break
        if pd.isna(data.signo):
            print("pd.isna(data.signo)")
            break
        if pd.isna(data.signo_cat):
            print("pd.isna(data.signo_cat)")
            break
        if pd.isna(data.genero):
            print("pd.isna(data.genero)")
            break
        if pd.isna(data.genero_cat):
            print("pd.isna(data.genero_cat)")
            break
        if pd.isna(data.direccion):
            print("pd.isna(data.direccion)")
            break
        if pd.isna(data.direccion_lat):
            print("pd.isna(data.direccion_lat)")
            break
        if pd.isna(data.direccion_lon):
            print("pd.isna(data.direccion_lon)")
            break
        if pd.isna(data.direccion_geo):
            print("pd.isna(data.direccion_geo)")
            break
        if pd.isna(data.pais):
            print("pd.isna(data.pais)")
            break
        if pd.isna(data.departamento):
            print("pd.isna(data.departamento)")
            break
        if pd.isna(data.municipio):
            print("pd.isna(data.municipio)")
            break
        if pd.isna(data.estado_civil):
            print("pd.isna(data.estado_civil)")
            break
        if pd.isna(data.estado_civil_cat):
            print("pd.isna(data.estado_civil_cat)")
            break
        if pd.isna(data.no_hijos):
            print("pd.isna(data.no_hijos)")
            break
        if pd.isna(data.grado_academico):
            print("pd.isna(data.grado_academico)")
            break
        if pd.isna(data.grado_academico_cat):
            print("pd.isna(data.grado_academico_cat)")
            break
        

        #print(data.apellido)
        db.session.add(data)
    db.session.commit()
    
#if __name__ == "__main__":
#    generateCliente()