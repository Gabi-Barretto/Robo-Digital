from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Boolean

#from sqlalchemy.ext.declarative import declarative_base
#Base = declarative_base()

class Base(DeclarativeBase):
    pass

class Coordenada(Base):
    __tablename__ = 'posicoes'
    id = Column(Integer, primary_key=True)
    x = Column(Integer)
    y = Column(Integer)
    z = Column(Integer)
  
    def __repr__(self):
        return f'Pessoa(id={self.id}, x={self.x}, y={self.y}, z={self.z})'

