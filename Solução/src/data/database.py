from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data.coordenadas import Base

def iniciar_banco_de_dados():
    engine = create_engine('sqlite:///posicao.db')
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)