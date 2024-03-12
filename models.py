from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Trees(Base):
    __tablename__ = "trees"
    id = Column(Integer, primary_key=True)
    tree_name = Column(String)
    tree_species = Column(String)
    tree_height = Column(Integer)