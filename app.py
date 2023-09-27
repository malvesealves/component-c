from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from model import Session, Pet, Responsavel, Endereco, Contato
from sqlalchemy.exc import IntegrityError

from model import Session, Pet
from logger import logger
from schemas import *
from flask_cors import CORS, cross_origin

info = Info(title="Cadastro de Pets API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
pet_tag = Tag(name="Pets", description="Adição, visualização e remoção de pets à base")
responsavel_tag = Tag(name="Responsável", description="Visualização de responsáveis de pets")
endereco_tag = Tag(name="Endereço", description="Visualização de endereço dos responsáveis de pets")
contato_tag = Tag(name="Contato", description="Visualização de contato dos responsáveis de pets")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/pet', tags=[pet_tag], responses={"200": PetViewSchema, "400": ErrorSchema})
def add_pet(form: PetSchema):
    """Adiciona um novo Pet à base de dados e Retorna uma representação dos items e comentários associados."""
    pet = Pet(
        artista=form.artista,
        descricao=form.descricao,
        formato=form.formato,)
    logger.debug(f"Adicionando item com o nome: '{pet.nome}'")
    try:
        session = Session()
        session.add(pet)
        session.commit()
        logger.debug(f"Adicionado item com o nome: '{pet.nomoe}'")
        return apresenta_pet(pet), 200

    except Exception as e:
        error_msg = "Não foi possível salvar novo pet :/"
        logger.warning(f"Erro ao adicionar pet '{pet.nome}', {error_msg}")
        return {"message": error_msg}, 400


@app.get('/pets', tags=[pet_tag], responses={"200": ListagemPetsSchema, "404": ErrorSchema})
def get_pets():
    """Faz a busca por todos os Pets cadastrados e retorna uma representação da listagem de pets."""
    logger.debug(f"Coletando items ")
    session = Session()
    items = session.query(Pet).all()

    if not items:
        return {"items": []}, 200
    else:
        logger.debug(f"%d items encontrados" % len(items))
        print(items)
        return apresenta_pets(items), 200


@app.get('/pet', tags=[pet_tag],
         responses={"200": PetViewSchema, "404": ErrorSchema})
def get_pet(query: PetBuscaSchema):
    """Faz a busca por um Pet a partir do id do pet

    Retorna uma representação dos pets e comentários associados.
    """
    pet_id = query.id
    logger.debug(f"Coletando dados sobre pet #{pet_id}")    
    session = Session()
    pet = session.query(Pet).filter(Pet.id == pet_id).first()

    if not pet:
        error_msg = "Pet não encontrado na base :/"
        logger.warning(f"Erro ao buscar pet '{pet_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Pet econtrado: '{pet.nome}'")        
        return apresenta_pet(pet), 200


@app.delete('/item', tags=[pet_tag], responses={"200": PetDelSchema, "404": ErrorSchema})
def del_item(query: PetBuscaSchema):
    """Deleta um Item a partir da descricao de item informado e retorna uma mensagem de confirmação da remoção."""
    item_descricao = (query.nome)
    print(item_descricao)
    logger.debug(f"Deletando dados sobre item #{item_descricao}")
    session = Session()
    count = session.query(Pet).filter(Pet.descricao == item_descricao).delete()
    session.commit()

    if count:
        logger.debug(f"Deletado item #{item_descricao}")
        return {"message": "Item removido", "id": item_descricao}
    else:
        error_msg = "Item não encontrado na base :/"
        logger.warning(f"Erro ao deletar item #'{item_descricao}', {error_msg}")
        return {"message": error_msg}, 404

@app.get('/responsaveis', tags=[responsavel_tag])
def get_responsaveis():
    """ Faz a busca por todos os responsáveis cadastrados na base de dados.

    Retorna para uma representação dos projetos.
    """
    logger.debug(f"Coletando Responsáveis")
    session = Session()
    responsaveis = session.query(Responsavel).all()

    if not responsaveis:
        return {"responsaveis": []}, 200
    else:
        logger.debug(f"%d Responsáveis encontradas" % len(responsaveis))
        result = []
        for responsavel in responsaveis:
            result.append(
                {
                    "id_responsavel": responsavel.id,
                    "nome": responsavel.nome
                }
            )
        return {"responsaveis": result}
    

@app.get('/enderecos', tags=[endereco_tag])
def get_enderecos():
    """ Faz a busca por todos os Endereços cadastrados na base de dados.

    Retorna para uma representação dos projetos.
    """
    logger.debug(f"Coletando Endereços")
    session = Session()
    enderecos = session.query(Endereco).all()

    if not enderecos:
        return {"enderecos": []}, 200
    else:
        logger.debug(f"%d Endereços encontrados" % len(enderecos))
        result = []
        for endereco in enderecos:
            result.append(
                {
                    "id_endereco": endereco.id,
                }
            )
        return {"enderecos": result}
    
@app.get('/contatos', tags=[contato_tag])
def get_contatos():
    """ Faz a busca por todos os Contatos cadastrados na base de dados.

    Retorna para uma representação dos projetos.
    """
    logger.debug(f"Coletando Contatos")
    session = Session()
    contatos = session.query(Contato).all()

    if not contatos:
        return {"contatos": []}, 200
    else:
        logger.debug(f"%d Contatos encontrados" % len(contatos))
        result = []
        for contato in contatos:
            result.append(
                {
                    "id_contato": contato.id,
                }
            )
        return {"contatos": result}
