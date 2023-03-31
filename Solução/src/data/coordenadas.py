from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()

class Coordenada(Base):
    __tablename__ = 'posicoes'
    id = Column(Integer, primary_key=True)
    x = Column(Integer)
    y = Column(Integer)
    z = Column(Integer)
  
    def __repr__(self):
        return f'Pessoa(id={self.id}, x={self.x}, y={self.y}, z={self.z})'

