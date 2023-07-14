from typing import List
from pydantic import BaseModel
from model.tipoanimal import TipoAnimal

class TipoContatoSchema(BaseModel):
    """ Define como um tipo de pet será retornado: nome.
    """
    nome: str = "cachorro"

class TipoContatoViewSchema(BaseModel):
    """ Define como um tipo de pet será retornado: nome.
    """
    nome: str = "cachorro"    


class ListagemTiposContatoSchema(BaseModel):
    """ Define como uma listagem de tipos de contatos será retornada.
    """
    nomes:List[TipoContatoSchema]

def apresenta_tipos_contato(tipos: List[TipoAnimal]):
    """ Retorna uma representação do tipo do petseguindo o schema definido em
        TipoContatoViewSchema.
    """
    result = []
    for tipo in tipos:
        result.append({
            "nome": tipo.nome,
        })

    return {"tipos_contato": result}