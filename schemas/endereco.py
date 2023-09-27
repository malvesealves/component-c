from pydantic import BaseModel

class EnderecoSchema(BaseModel):
    """ Define como um endereço deve ser representado
    """
    id_endereco: int = 1
    cep: str = "12345678"
    logradouro: str = "Rua A"
    complemento: str = "Apto 1"
    bairro: str = "Bairro A"
    localidade: str = "Rio de Janeiro"
    uf: str = "RJ"