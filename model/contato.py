from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from model import Base

class Contato(Base):
    __tablename__ = 'contato'

    id = Column("id_contato", Integer, primary_key=True)
    ddd = Column(String(3))
    numero = Column(String(10),primary_key=True)    
    responsavel = relationship('Responsavel')
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, ddd: str, descricao: str, data_insercao:Union[DateTime, None] = None):
        """
        Cria o contato para responsável pelo pet

        Arguments:
            ddd: ddd do contato do responsável pelo pelo
            numero: número do contato do responsável pelo pelo
            data_insercao: data de quando o contato foi inserido à base
        """
        self.ddd = ddd
        self.numero = descricao

        if data_insercao:
            self.data_insercao = data_insercao