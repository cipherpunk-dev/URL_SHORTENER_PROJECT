from sqlalchemy import create_engine  #basic engine creation
from sqlalchemy.ext.declarative import declarative_base   #use of Base model classes
from sqlalchemy.orm import sessionmaker   #establish sesssion between db and python

from . config import get_settings

#creating engine reqs path to sqlite/other 
#check same thread set to false to allow multiple users access same thread
engine=create_engine(get_settings().db_url,connect_args={"check_same_thread":False})
#auto commit false to ensure atomicity (ACID)
#auto flush to false for similar reasons
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()  
