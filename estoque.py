"""Camada de dados do estoque: persistência em JSON e operações de CRUD."""

import json
import os

ARQUIVO_DADOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "estoque.json")


def carregar_estoque():
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []


def salvar_estoque(estoque):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(estoque, arquivo, ensure_ascii=False, indent=4)


def proximo_id(estoque):
    if not estoque:
        return 1
    return max(produto["id"] for produto in estoque) + 1


def encontrar_produto(estoque, produto_id):
    for produto in estoque:
        if produto["id"] == produto_id:
            return produto
    return None


def cadastrar_produto(estoque, nome, quantidade, preco):
    produto = {
        "id": proximo_id(estoque),
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco,
    }
    estoque.append(produto)
    salvar_estoque(estoque)
    return produto


def atualizar_produto(estoque, produto_id, nome=None, quantidade=None, preco=None):
    produto = encontrar_produto(estoque, produto_id)
    if produto is None:
        return None
    if nome is not None:
        produto["nome"] = nome
    if quantidade is not None:
        produto["quantidade"] = quantidade
    if preco is not None:
        produto["preco"] = preco
    salvar_estoque(estoque)
    return produto


def remover_produto(estoque, produto_id):
    produto = encontrar_produto(estoque, produto_id)
    if produto is None:
        return None
    estoque.remove(produto)
    salvar_estoque(estoque)
    return produto


def buscar_por_nome(estoque, termo):
    termo = termo.lower()
    return [produto for produto in estoque if termo in produto["nome"].lower()]


def produtos_estoque_baixo(estoque, limite=5):
    return [produto for produto in estoque if produto["quantidade"] <= limite]


def valor_total_estoque(estoque):
    return sum(produto["quantidade"] * produto["preco"] for produto in estoque)
