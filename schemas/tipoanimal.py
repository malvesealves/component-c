from pydantic import BaseModel
from typing import List
from model.tipoanimal import TipoAnimal

class TipoAnimalSchema(BaseModel):
    """ Define como um tipo de pet será retornado: nome.
    """
    nome: str = "cachorro"

class TipoAnimalViewSchema(BaseModel):
    """ Define como um tipo de pet será retornado: nome.
    """
    nome: str = "cachorro"    


class ListagemTiposAnimalPetSchema(BaseModel):
    """ Define como uma listagem de tipos de animal será retornada.
    """
    nomes:List[TipoAnimalSchema]

def apresenta_tipos_animal(tipos: List[TipoAnimal]):
    """ Retorna uma representação do tipo do petseguindo o schema definido em
        TipoAnimalViewSchema.
    """
    result = []
    for tipo in tipos:
        result.append({
            "nome": tipo.nome,
        })

    return {"tipos_animal": result}