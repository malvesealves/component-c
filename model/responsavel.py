from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from model import Base

class Responsavel(Base):
    __tablename__ = 'responsavel'

    id = Column("id_responsavel", Integer, primary_key=True)
    nome = Column(String(100))    
    pet = relationship('Pet')
    id_contato = Column(Integer, ForeignKey("contato.id_contato"), nullable=False)
    contato = relationship('Contato')
    id_endereco = Column(Integer, ForeignKey("endereco.id_endereco"), nullable=False)
    endereco = relationship('Endereco')
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome: str, id_contato: Integer, id_endereco: Integer, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Responsável de Pet

        Arguments:
            nome: nome do responsável a ser cadastrado
            idade: idade do pet
            data_insercao: data de quando o pet foi inserido à base
        """
        self.nome = nome
        self.id_contato = id_contato
        self.id_endereco = id_endereco

        if data_insercao:
            self.data_insercao = data_insercao