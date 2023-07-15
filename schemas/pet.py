from pydantic import BaseModel
from typing import Optional, List
from model.pet import Pet


class PetSchema(BaseModel):
    """ Define como um novo pet a ser inserido deve ser representado
    """
    nome: str = "Scooby-Doo"
    idade: Optional[int] = 12
    responsavel: str = "Salsicha"


class PetBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita com base no nome do pet.
    """
    nome: str = "Teste"


class ListagemPetsSchema(BaseModel):
    """ Define como uma listagem de pets será retornada.
    """
    pets:List[PetSchema]


def apresenta_pets(pets: List[Pet]):
    """ Retorna uma representação do pet seguindo o schema definido em
        PetViewSchema.
    """
    result = []
    for pet in pets:
        result.append({
            "nome": pet.nome,
            "idade": pet.idade,
            "responsavel": pet.responsavel
        })

    return {"pets": result}


class PetViewSchema(BaseModel):
    """ Define como um pet será retornado: pet.
    """
    id: int = 1
    nome: str = "Scooby-Doo"
    idade: Optional[int] = 12
    responsavel: str = "Salsicha"


class PetDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_pet(pet: Pet):
    """ Retorna uma representação do pet seguindo o schema definido em
        PetViewSchema.
    """
    return {
        "id": pet.id,
        "nome": pet.nome,
        "idade": pet.idade,
        "responsavel": pet.responsavel
    }
