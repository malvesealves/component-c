from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Pet
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Cadastro de Cachorro API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
pet_tag = Tag(name="Pet", description="Adição, visualização e remoção de pets à base")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/pet', tags=[pet_tag],
          responses={"200": PetViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_pet(form: PetSchema):
    """Adiciona um novo pet à base de dados

    Retorna uma representação dos pets e comentários associados.
    """
    pet = Pet(
        nome=form.nome,
        quantidade=form.quantidade,
        valor=form.valor)
    logger.debug(f"Adicionando pet de nome: '{pet.nome}'")
    try:
        session = Session()
        session.add(pet)
        session.commit()
        logger.debug(f"Adicionado pet de nome: '{pet.nome}'")
        return apresenta_pet(pet), 200

    except IntegrityError as e:
        error_msg = "Pet de mesmo nome e tipo já salvo na base :/"
        logger.warning(f"Erro ao adicionar pet ({pet.tipo})'{pet.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar pet '{pet.nome}', {error_msg}")
        return {"message": error_msg}, 400


@app.get('/pets', tags=[pet_tag],
         responses={"200": ListagemPetsSchema, "404": ErrorSchema})
def get_pets():
    """Faz a busca por todos os pets cadastrados

    Retorna uma representação da listagem de pets.
    """
    logger.debug(f"Coletando pets ")
    session = Session()
    pets = session.query(Pet).all()

    if not pets:
        return {"pets": []}, 200
    else:
        logger.debug(f"%d pets encontrados" % len(pets))
        print(pets)
        return apresenta_pets(pets), 200


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


@app.delete('/pet', tags=[pet_tag],
            responses={"200": PetDelSchema, "404": ErrorSchema})
def del_pet(query: PetBuscaSchema):
    """Deleta um Pet a partir do nome de pet informado

    Retorna uma mensagem de confirmação da remoção.
    """
    pet_nome = unquote(unquote(query.nome))
    print(pet_nome)
    logger.debug(f"Deletando dados sobre pet #{pet_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Pet).filter(Pet.nome == pet_nome).delete()
    session.commit()

    if count:        
        logger.debug(f"Deletado pet #{pet_nome}")
        return {"mesage": "Pet removido", "id": pet_nome}
    else:
        error_msg = "Pet não encontrado na base :/"
        logger.warning(f"Erro ao deletar pet #'{pet_nome}', {error_msg}")
        return {"message": error_msg}, 404