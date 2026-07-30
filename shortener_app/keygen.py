import secrets #for generating random keys(better h random se)
import string
from . import crud
from sqlalchemy.orm import Session
def create_r_key(length:int = 5)->str:
    chars=string.ascii_uppercase+string.digits
    return "".join(secrets.choice(chars) for _ in range(length))
def create_random_key(db:Session,length:int =5)->str:
    key=create_r_key(length)
    while crud.get_db_url_by_key(db,key):
        key=create_r_key(length)
    return key;