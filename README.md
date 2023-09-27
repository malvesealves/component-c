# Pós-Graduação em Engenharia de Software - MVP SPRINT 2 

Componente C - API Python para cadastro de pets

---
## Como executar 

Requisitos:
- É necessário possuir o [Docker](https://docs.docker.com/engine/install/) instalado e em execução.

Etapas:


1 - Clonar o repositório e descompactar da pasta .zip.

2 - Ir ao diretório raiz, onde contém o Dockerfile, e executar como administrador o seguinte comando para construir a imagem Docker:
```
$ docker build -t component-c-api
```

3 - Após a criação da imagem, executar como adminitrador o seguinte comando para rodar o container:
```
$ docker run -p 8000:80 componen-c-api
```

Após seguir todos os passos, abrir o link abaixo no bavegador para verificar o status da API em execução
- [http://localhost:8000/#/](http://localhost:8000/#/)

