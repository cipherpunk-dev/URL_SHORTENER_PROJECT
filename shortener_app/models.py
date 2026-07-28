from sqlalchemy import BOOLEAN,Integer,Text,String,Column
from . database import Base
class URL(Base):
    __tablename__="urls"
    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True) #index ka kaam h for O log N lookup
    secret_key = Column(String, unique=True, index=True)
    target_url = Column(String, index=True)
    is_active = Column(BOOLEAN, default=True)
    clicks = Column(Integer, default=0)