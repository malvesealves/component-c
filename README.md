# Objetivo

A proposta do MVP é de desenvolver projeto destinado a buscar, cadastrar e remover cães e gatos em uma clínica veterinária.

Este repositório comporta a parte do backend do projeto na qual encontra-se a API construída.

Projeto entregue para a Sprint 1 - Desenvolvimento Full Stack do curso de Pós-Graduação em Engenharia de Software da PUC-Rio.


## Execução

Primeiramente é necessário clonar o repositório, em seguida se faz necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos a seguir nas instruções.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Para instalação do ambiente virtual, recomenda-se utilizar o gerenciador de pacotes pip, originalmente instalado junto com o Python.

```
$ pip install virtualenv
```

Em seguida, será criado ambiente virtual com o comando

```
$ virtualenv venv
```

A ativação do ambiente virtual será feita com o comando

```
$ source venv/scripts/activate
```

Seguimos para a instalação das libs python listadas no `requirements.txt` através do comando

```
(venv)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Atenção: Caso a versão do Python utilizada seja 3.11.4 (na qual o projeto foi desenvolvido) ou superior, será necessário instalar a biblioteca greenlet separadamente através do comando

```
(venv)$ pip install greenlet
```

Para executar a API  basta executar:

```
(venv)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(venv)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
