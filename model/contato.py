from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from  model import Base


class Contato(Base):
    __tablename__ = 'contato'

    id = Column(Integer, primary_key=True)
    responsavel = Column(String(200))
    contato = Column(String(4000))
    data_insercao = Column(DateTime, default=datetime.now())

    tipo_contato = Column(Integer, ForeignKey("tipo_contato.pk_tipo_contato"), unique=True, nullable=False )
    pet = Column(Integer, ForeignKey("pet.pk_pet"), unique=False, nullable=False)

    def __init__(self, responsavel: str, contato:str, tipo_contato: int, pet: int, data_insercao:Union[DateTime, None] = None):
        """
        Cria um Contato

        Arguments:
            responsavel: nome do responsável
            texto: o contato do responsável.
            data_insercao: data de quando o contato do responsável foi inserido à base
        """
        self.responsavel = responsavel
        self.contato = contato
        self.tipo_contato = tipo_contato
        self.pet = pet
        if data_insercao:
            self.data_insercao = data_insercao
