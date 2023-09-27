from pydantic import BaseModel

class ResponsavelSchema(BaseModel):
    """ Define como um responsavel deve ser representado
    """
    id_responsavel: int = 1
    nome: str = "Mateus"
    id_contato: int = 1
    id_endereco: int = 1