from pydantic import BaseModel as PydanticBaseModel
from typing import List
from model.pet import Pet
from model.responsavel import Responsavel
from model.contato import Contato
from model.endereco import Endereco

class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True

class PetSchema(BaseModel):
    """ Define como um novo pet a ser inserido deve ser representado"""
    tipo: str = "Cachorro"
    nome: str = "Thor"
    idade: str = "1"
    id_responsavel: int = 1

class PetBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita com base no nome do pet.
    """
    nome: str = "Teste"

class PetViewSchema(BaseModel):
    """ Define como um pet será retornado: pet"""
    tipo: str = "Cachorro"
    nome: str = "Thor"
    responsavel: str = "Mateus"
    id_responsavel: str = 1

class ListagemPetsSchema(BaseModel):
    """ Define como uma listagem de pets será retornada."""
    pets:List[PetSchema]

class PetBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será feita apenas com base no nome do pet."""
    nome: str = "Thor"

class PetDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de remoção."""
    message: str
    descricao: str

def apresenta_pets(pets: List[Pet]):
    """ Retorna uma representação do pet seguindo o schema definido em PetViewSchema."""
    result = []
    for pet in pets:
        result.append({
            "tipo": pet.tipo,
            "nome": pet.nome,
            "responsavel": pet.responsavel,
            "contato": pet.responsavel.contato,
            "endereco": pet.responsavel.endereco
        })
    return {"pets": result}

class PetViewSchema(BaseModel):
    """ Define como um pet será retornado: pet.
    """
    id: int = 1
    nome: str = "Scooby-Doo"
    idade: int = 1
    responsavel: str = "Salsicha"


class PetDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_pet(pet: Pet):
    """ Retorna uma representação do pet seguindo o schema definido em PetViewSchema."""
    return {
        "tipo": pet.tipo,
        "nome": pet.nome,
        "responsavel": pet.responsavel,
        "contato": pet.responsavel.contato,
        "endereco": pet.responsavel.endereco
    }
