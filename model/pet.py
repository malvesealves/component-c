from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Contato


class Pet(Base):
    __tablename__ = 'pet'

    id = Column("pk_pet", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    idade = Column(Integer)
    data_insercao = Column(DateTime, default=datetime.now())

    tipo_animal = Column(Integer, ForeignKey("tipo_animal.pk_tipo_animal"), unique=True, nullable=False )

    contatos = relationship("Contato")

    def __init__(self, tipo_animal:int, nome:str, idade:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um pet

        Arguments:
            tipo: tipo de pet
            nome: nome do pet
            idade: idade do pet
            data_insercao: data de quando o pet foi inserido à base
        """
        self.tipo_animal = tipo_animal
        self.nome = nome
        self.idade = idade

        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_contato(self, contato:Contato):
        """ Adiciona um novo contato de responsável ao Pet
        """
        self.contatos.append(contato)

