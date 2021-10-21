from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

provider = "mysql+pymysql"
database ="intneg_dev"
#server= "10.70.70.30"
server= ""
port= "3306"
user= ""
password= ""

#engine = create_engine("mysql+pymysql://vachocalla:12345678.Nueve@10.70.70.30/intneg?charset=utf8mb4")
engine = create_engine(provider+"://"+user+":"+password+"@"+server+"/"+database+"?charset=utf8mb4")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()