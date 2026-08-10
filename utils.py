"""Funções utilitárias de terminal e leitura validada de dados."""

import os


def limpar_tela():
    """Limpa o terminal (Windows ou Unix)."""
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPressione ENTER para continuar...")


def ler_inteiro(mensagem, minimo=None):
    while True:
        valor = input(mensagem).strip()
        try:
            numero = int(valor)
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
            continue
        if minimo is not None and numero < minimo:
            print(f"O valor deve ser maior ou igual a {minimo}.")
            continue
        return numero


def ler_float(mensagem, minimo=None):
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            numero = float(valor)
        except ValueError:
            print("Valor inválido. Digite um número (ex: 19.90).")
            continue
        if minimo is not None and numero < minimo:
            print(f"O valor deve ser maior ou igual a {minimo}.")
            continue
        return numero


def ler_texto(mensagem, obrigatorio=True):
    while True:
        valor = input(mensagem).strip()
        if obrigatorio and not valor:
            print("Este campo não pode ficar em branco.")
            continue
        return valor
