from pydantic import BaseModel


class ContatoSchema(BaseModel):
    """ Define como um novo comentário a ser inserido deve ser representado
    """
    pet_id: int = 1
    tipo_contato_id: int = 1
    texto: str = "Só comprar se o preço realmente estiver bom!"
