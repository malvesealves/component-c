from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from model import Base

class Pet(Base):
    __tablename__ = 'pet'

    id = Column("id_pet", Integer, primary_key=True)
    tipo = Column(String(50))
    nome = Column(String(100),primary_key=True)
    idade = Column(String(50))
    id_responsavel = Column(Integer, ForeignKey("responsavel.id_responsavel"), nullable=False)
    responsavel = relationship('Responsavel')
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, tipo: str, nome: str, idade: str, id_responsavel: Integer, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Pet

        Arguments:
            tipo: tipo de pet
            nome: nome do pet a ser cadastrado
            idade: idade do pet
            data_insercao: data de quando o pet foi inserido à base
        """
        self.tipo = tipo
        self.nome = nome
        self.idade = idade
        self.id_responsavel = id_responsavel

        if data_insercao:
            self.data_insercao = data_insercao