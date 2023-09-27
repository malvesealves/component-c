from pydantic import BaseModel

class ContatoSchema(BaseModel):
    """ Define como um contato deve ser representado
    """
    id_contato: int = 1
    ddd: str = "021"
    numero: str = "123456789"