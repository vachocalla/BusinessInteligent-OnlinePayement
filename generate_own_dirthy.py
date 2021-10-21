import random, time, datetime 
from numpy.random import randint

def generarEdad():
    rand = random.random()
    return random.randint(-20, 13) if rand<=0.01 \
    else ( random.randint(90, 250) if rand>=0.98 else random.randint(13, 90) )
#--------------------------------------------------
def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))

def generate_date():
    try:
        rand = random.random()
        return str_time_prop("1/1/1920", "31/12/1969", '%d/%m/%Y', random.random()) if rand<=0.01 else ( str_time_prop("1/1/2008", "31/12/2150", '%d/%m/%Y', random.random()) if rand>=0.98 else str_time_prop("1/1/1970", "31/12/2007", '%d/%m/%Y', random.random()) )
    except Exception as e: # work on python 2.x
        return generate_date()

def generarGenero():
    genero = ['Masculino','Femenino','M','F','masculino','femenino']
    rand = random.random()
    return None if rand<=0.01 else ( None if rand>=0.99 else genero[random.randint(0, len(genero)-1)] )

def generarPais():
    depto = ['Bolivia','bo','Bol','BO']
    rand = random.random()
    return None if rand<=0.01 else ( None if rand>=0.99 else depto[random.randint(0, len(depto)-1)] )
#--------------------------------------------------

def generarDepartamento():
    depto = ['Oruro','or','Cbba','Cochabamba ','Santa Cruz','Sc ','La Paz','LP','Pando','pa','Beni','BE','Sucre','Su','Tarija','tj','Potosi','pt']
    rand = random.random()
    return None if rand<=0.01 else ( None if rand>=0.99 else depto[random.randint(0, len(depto)-1)] )
#--------------------------------------------------

def generarEC():
    ec = ['Solter@','Casad@','Viud@','Concubinad@','Divociad@']
    rand = random.random()
    return None if rand<=0.01 else ( None if rand>=0.99 else ec[random.randint(0, len(ec)-1)] )
#--------------------------------------------------

def generarNoHijos():
    rand = random.random()
    return random.randint(-10, -1) if rand<=0.01 else ( random.randint(9, 99) if rand>=0.99 else random.randint(0, 8) )
#--------------------------------------------------

def generarGradoAcademico(born0):
    born = datetime.datetime.strptime(born0, '%d/%m/%Y')
    today = datetime.date.today()
    edad = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    rand = random.random()
    if edad<=16:
        return None if rand<=0.02 else 'Ninguno'
    elif edad<=27:
        return None if rand<=0.02 else ( ( 'Ninguno' if rand<=0.25 else 'Bachiller' ) if rand<=0.69 else 'Licenciatura' )
    elif edad<=37:
        return None if rand<=0.02 else ( ( None if rand<=0.02 else ( ( 'Ninguno' if rand<=0.25 else 'Bachiller' ) if rand<=0.69 else 'Licenciatura' ) ) if rand<=0.89 else 'Maestria' )
    else:
        return None if rand<=0.02 else ( None if rand<=0.02 else ( ( None if rand<=0.02 else ( ( 'Ninguno' if rand<=0.25 else 'Bachiller' ) if rand<=0.69 else 'Licenciatura' ) ) if rand<=0.89 else 'Maestria' ) ) if rand<=0.96 else 'Doctorado'

#--------------------------------------------------
def generarTamanoEmpresa():
    rand = random.random()
    return random.randint(-100, -1) if rand<=0.01 else ( random.randint(25, 1000) if rand<=0.15 else ( random.randint(10, 26) if rand<=0.55 else random.randint(1, 10) ) )

#--------------------------------------------------
def generarPrecio():
    rand = random.random()
    return None if rand<=0.01 else ( random.randint(-100, -1) if rand>=0.98 else random.randint(10, 500) )
#--------------------------------------------------
