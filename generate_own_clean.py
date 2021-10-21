import random,time, datetime 
from numpy.random import randint
import seed_data.nacimientoGeo

#--------------------------------------------------
def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))

# [ (from, to, percent) ]
def generate_date_birthday(data):
    try:
        rand = random.random()
        i=0
        while( i<len(data) ):
            if rand<data[i][2]: 
                #return str_time_prop("1/1/1920", "31/12/1969", '%d/%m/%Y', random.random()) if rand<=0.01 else ( str_time_prop("1/1/2008", "31/12/2150", '%d/%m/%Y', random.random()) if rand>=0.98 else str_time_prop("1/1/1970", "31/12/2007", '%d/%m/%Y', random.random()) )
                return str_time_prop(data[i][0], data[i][1], '%d/%m/%Y', random.random())
            i=i+1
        #
    except Exception as e: # work on python 2.x
        return generate_date_birthday(data)

def to_milliseconds(dt):
	epoch = datetime.datetime.utcfromtimestamp(0)
	return (dt - epoch).total_seconds() * 1000

def programZodiac(date):
    Day = date.timetuple().tm_yday
    Month = date.strftime("%m")

    if ((int(Month)==12 and int(Day) >= 22)or(int(Month)==1 and int(Day)<= 19)):
        return ("Capricorn",1)
    elif ((int(Month)==1 and int(Day) >= 20)or(int(Month)==2 and int(Day)<= 17)):
            return ("aquarium",2)
    elif ((int(Month)==2 and int(Day) >= 18)or(int(Month)==3 and int(Day)<= 19)):
            return ("Pices",3)
    elif ((int(Month)==3 and int(Day) >= 20)or(int(Month)==4 and int(Day)<= 19)):
            return ("Aries",4)
    elif ((int(Month)==4 and int(Day) >= 20)or(int(Month)==5 and int(Day)<= 20)):
            return ("Taurus",5)
    elif ((int(Month)==5 and int(Day) >= 21)or(int(Month)==6 and int(Day)<= 20)):
            return ("Gemini",6)
    elif ((int(Month)==6 and int(Day) >= 21)or(int(Month)==7 and int(Day)<= 22)):
            return ("Cancer",7)
    elif ((int(Month)==7 and int(Day) >= 23)or(int(Month)==8 and int(Day)<= 22)): 
            return ("Leo",8)
    elif ((int(Month)==8 and int(Day) >= 23)or(int(Month)==9 and int(Day)<= 22)): 
            return ("Virgo",9)
    elif ((int(Month)==9 and int(Day) >= 23)or(int(Month)==10 and int(Day)<= 22)):
            return ("Libra",10)
    elif ((int(Month)==10 and int(Day) >= 23)or(int(Month)==11 and int(Day)<= 21)): 
            return ("Scorpio",11)
    elif ((int(Month)==11 and int(Day) >= 22)or(int(Month)==12 and int(Day)<= 21)):
            return ("Sagittarius",12)

    return ("",0)

def generarGenero():
    genero = ['Masculino','Femenino','M','F','masculino','femenino']
    genero_Cat = ['M','F','M','F','M','F']
    rand = random.randint(0, len(genero)-1)
    return genero[rand],genero_Cat[rand]

def generarLugar():
    data = seed_data.nacimientoGeo.rangoEtario
    rand = random.random()
    i=0
    while( i<len(data) ):
        if rand<data[i][0]:
            lat = 0
            lon = 0
            randLoc = random.random()
            j=0
            while( j<len(data[i][2]) ):
                if randLoc<data[i][2][j][4]:
                    lat = random.uniform( data[i][2][j][0] , data[i][2][j][2])
                    lon = random.uniform( data[i][2][j][1] , data[i][2][j][3])
                    j=len(data[i][2])
                j=j+1
            return (data[i][1],lat,lon)
        i=i+1

def generarLugarDepartamento(depto):
    data = seed_data.nacimientoGeo.rangoEtario
    #rand = random.random()
    i=0
    while( i<len(data) ):
        if depto==data[i][1]:
            lat = 0
            lon = 0
            randLoc = random.random()
            j=0
            while( j<len(data[i][2]) ):
                if randLoc<data[i][2][j][4]:
                    lat = random.uniform( data[i][2][j][0] , data[i][2][j][2])
                    lon = random.uniform( data[i][2][j][1] , data[i][2][j][3])
                    j=len(data[i][2])
                j=j+1
            return (data[i][1],lat,lon)
        i=i+1


def generarEC(fnDate):
    ec = ['Solter@','Casad@','Viud@','Concubinad@','Divociad@']
    ec_cat = ['S','C','V','J','D']
    today = datetime.date.today()
    edad = today.year - fnDate.year - ((today.month, today.day) < (fnDate.month, fnDate.day))
    if  edad<18:
        # ec,ec_cat,nohijos,
        return (ec[0],ec_cat[0],random.randint(0, 1) )
    else:
        rand = random.random()
        if rand<0.15:
            return (ec[0],ec_cat[0],random.randint(0, 3) )
        elif rand<0.65:
            return (ec[1],ec_cat[1],random.randint(1, 4) )
        elif rand<0.75:
            return (ec[2],ec_cat[2],random.randint(1, 4) )
        elif rand<0.85:
            return (ec[3],ec_cat[3],random.randint(0, 2) )
        else:
            return (ec[4],ec_cat[4],random.randint(0, 3) )

def generarGradoAcademico(born0):
    born = datetime.datetime.strptime(born0, '%d/%m/%Y')
    today = datetime.date.today()
    edad = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    rand = random.random()
    if edad<=16:
        return ('Ninguno',0)
    elif edad<=27:
        return ( ('Ninguno',0) if rand<=0.25 else ('Bachiller',1) ) if rand<=0.69 else ('Licenciatura',2) 
    elif edad<=37:
        return ('Ninguno',0) if rand<=0.17 else ( ('Bachiller',1) if rand<=0.57 else ( ('Licenciatura',2) if rand<=0.83 else ('Maestria',3) ) )
    else:
        return ('Ninguno',0) if rand<=0.17 else ( ('Bachiller',1) if rand<=0.57 else ( ('Licenciatura',2) if rand<=0.83 else ( ('Maestria',3) if rand<=0.96 else ('Doctorado',4) ) ) )

def generarTamanoEmpresa():
    return random.randint(1, 150)
