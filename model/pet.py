from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base


class Pet(Base):
    __tablename__ = 'pet'

    id = Column("pk_pet", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    idade = Column(Integer, nullable=True)
    responsavel = Column(String(150))
    data_insercao = Column(DateTime, default=datetime.now())


    def __init__(self, nome:str, idade:int,
                 responsavel:str, data_insercao:Union[DateTime, None] = None):
        """
        Cria um pet

        Arguments:
            nome: nome do pet
            idade: idade do pet
            responsavel: responsável do pet
            data_insercao: data de quando o pet foi inserido à base
        """        
        self.nome = nome
        self.idade = idade
        self.responsavel = responsavel

        if data_insercao:
            self.data_insercao = data_insercao