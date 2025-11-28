 API de Produtos (FastAPI)

Este projeto é uma API simples para cadastro de produtos.  
Foi desenvolvida para estudo de rotas, CRUD e modelos com FastAPI e Pydantic.

* Funcionalidades:
- Criar produto
- Listar todos os produtos
- Ver um produto específico
- Deletar produto
- Armazenamento em memória (lista)

* Tecnologias:
- Python
- FastAPI
- Uvicorn
- Pydantic

* Estrutura do projeto:
main.py  
models.py

* Como executar:
1. Instale as dependências:
   pip install fastapi uvicorn

2. Rode o servidor:
   uvicorn main:app --reload

3. Acesse:
   API: http://127.0.0.1:8000  
   Documentação: http://127.0.0.1:8000/docs

* Objetivo do projeto:
Treinar desenvolvimento de APIs com Python usando FastAPI, criando um CRUD básico para estudo.
