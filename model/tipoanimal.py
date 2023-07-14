from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from  model import Base

class TipoAnimal(Base):
    __tablename__ = 'tipo_animal'

    id = Column("pk_tipo_animal", Integer, primary_key=True)
    nome = Column(String(200))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, data_insercao:Union[DateTime, None] = None):
        """
        Cria um tipo

        Arguments:
            nome: nome do tipo do animal
            data_insercao: data de quando o pet foi inserido à base
        """
        self.nome = nome

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao