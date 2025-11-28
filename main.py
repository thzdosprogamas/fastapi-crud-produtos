#Quero uma API simples para cadastrar produtos de uma loja. Preciso conseguir criar produtos, 
# listar todos, ver um produto específico, atualizar e deletar. Não precisa de banco de dados, pode ser lista na memória."

from fastapi import FastAPI
from models import Produto

app = FastAPI()

# Banco de dados temporário
produtos = []


@app.get("/")
def homepage():
    return {"mensagem": "API funcionando, forte abraçoz!"}


# =========================
# LISTAR TODOS
# =========================
@app.get("/produtos")
def listar_produtos():
    return produtos


# =========================
# CRIAR PRODUTO
# =========================
@app.post("/produtos")
def criar_produto(prod: Produto):
    produtos.append(prod)
    return {"mensagem": "Produto criado!", "dados": prod}


# =========================
# LER UM PRODUTO ESPECÍFICO
# =========================
@app.get("/produtos/{nome}")
def ver_produto(nome: str):
    for p in produtos:
        if p.nome == nome:
            return p
    return {"erro": "Produto não encontrado"}


# =========================
# DELETAR PRODUTO
# =========================
@app.delete("/produtos/{nome}")
def deletar_produto(nome: str):
    for p in produtos:
        if p.nome == nome:
            produtos.remove(p)
            return {"mensagem": "Deletado com sucesso!"}
    return {"erro": "Produto não encontrado"}
