from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://vach:12345@10.70.70.30/intneg?charset=utf8mb4")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()