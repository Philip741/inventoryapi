from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date
from .database import Base

class Record(Base):
    __tablename__ = "Inventory"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    servername = Column(String(255), index=True)
    ip_address = Column(String(25))
    
    