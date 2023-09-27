from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from model import Base

class Endereco(Base):
    __tablename__ = 'endereco'

    id = Column("id_endereco", Integer, primary_key=True)
    cep = Column(String(10))
    logradouro = Column(String(150))
    complemento = Column(String(100))
    bairro = Column(String(100))
    localidade = Column(String(100))
    uf = Column(String(2))
    responsavel = relationship('Responsavel')
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, cep: str, logradouro: str, complemento: str, bairro: str, localidade: str, uf: str, data_insercao:Union[DateTime, None] = None):
        """
        Cria o endereço para responsável pelo pet

        Arguments:
            cep: cep do endereço do responsável pelo pet
            logradouro: logradouro do endereço do responsável pelo pet
            complemento: complemento do endereço do responsável pelo pet
            bairro: bairro do endereço do responsável pelo pet
            localidade: localidade do endereço do responsável pelo pet
            data_insercao: data de quando o endereço foi inserido à base
        """
        self.cep = cep
        self.logradouro = logradouro
        self.complemento = complemento
        self.bairro = bairro
        self.localidade = localidade
        self.uf = uf

        if data_insercao:
            self.data_insercao = data_insercao