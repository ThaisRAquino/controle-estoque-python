"""Sistema de Controle de Estoque - Loja de Eletrônicos."""

from estoque import (
    atualizar_produto,
    buscar_por_nome,
    cadastrar_produto,
    carregar_estoque,
    produtos_estoque_baixo,
    remover_produto,
    valor_total_estoque,
)
from utils import ler_float, ler_inteiro, ler_texto, limpar_tela, pausar

LIMITE_ESTOQUE_BAIXO = 5


def exibir_menu():
    print("=" * 42)
    print("  CONTROLE DE ESTOQUE - LOJA DE ELETRÔNICOS")
    print("=" * 42)
    print("[1] Listar produtos")
    print("[2] Cadastrar novo produto")
    print("[3] Atualizar produto")
    print("[4] Remover produto")
    print("[5] Buscar produto por nome")
    print("[6] Relatório de estoque baixo")
    print("[7] Valor total em estoque")
    print("[0] Sair")
    print("=" * 42)


def listar_produtos(estoque):
    if not estoque:
        print("\nNenhum produto cadastrado.")
        return
    print(f"\n{'ID':<5}{'Nome':<25}{'Qtd':<8}{'Preço':<12}")
    print("-" * 50)
    for produto in estoque:
        print(
            f"{produto['id']:<5}{produto['nome']:<25}"
            f"{produto['quantidade']:<8}R$ {produto['preco']:.2f}"
        )


def menu_cadastrar(estoque):
    print("\n--- Cadastrar novo produto ---")
    nome = ler_texto("Nome do produto: ")
    quantidade = ler_inteiro("Quantidade em estoque: ", minimo=0)
    preco = ler_float("Preço (R$): ", minimo=0)
    produto = cadastrar_produto(estoque, nome, quantidade, preco)
    print(f"\nProduto '{produto['nome']}' cadastrado com ID {produto['id']}.")


def menu_atualizar(estoque):
    listar_produtos(estoque)
    if not estoque:
        return
    produto_id = ler_inteiro("\nInforme o ID do produto a atualizar: ")

    print("Deixe em branco para manter o valor atual.")
    nome = input("Novo nome: ").strip() or None

    quantidade = None
    quantidade_texto = input("Nova quantidade: ").strip()
    if quantidade_texto:
        try:
            quantidade = int(quantidade_texto)
        except ValueError:
            print("Quantidade inválida, valor mantido.")

    preco = None
    preco_texto = input("Novo preço: ").strip().replace(",", ".")
    if preco_texto:
        try:
            preco = float(preco_texto)
        except ValueError:
            print("Preço inválido, valor mantido.")

    produto = atualizar_produto(estoque, produto_id, nome, quantidade, preco)
    if produto:
        print(f"\nProduto ID {produto_id} atualizado com sucesso.")
    else:
        print(f"\nProduto com ID {produto_id} não encontrado.")


def menu_remover(estoque):
    listar_produtos(estoque)
    if not estoque:
        return
    produto_id = ler_inteiro("\nInforme o ID do produto a remover: ")
    confirmacao = input("Confirma a remoção? (s/n): ").strip().lower()
    if confirmacao != "s":
        print("Operação cancelada.")
        return
    produto = remover_produto(estoque, produto_id)
    if produto:
        print(f"\nProduto '{produto['nome']}' removido.")
    else:
        print(f"\nProduto com ID {produto_id} não encontrado.")


def menu_buscar(estoque):
    termo = ler_texto("\nDigite o nome (ou parte dele) para buscar: ")
    resultados = buscar_por_nome(estoque, termo)
    if not resultados:
        print("Nenhum produto encontrado.")
        return
    listar_produtos(resultados)


def menu_estoque_baixo(estoque):
    resultados = produtos_estoque_baixo(estoque, LIMITE_ESTOQUE_BAIXO)
    if not resultados:
        print(f"\nNenhum produto com estoque igual ou abaixo de {LIMITE_ESTOQUE_BAIXO} unidades.")
        return
    print(f"\nProdutos com estoque baixo (<= {LIMITE_ESTOQUE_BAIXO} unidades):")
    listar_produtos(resultados)


def main():
    estoque = carregar_estoque()
    while True:
        limpar_tela()
        exibir_menu()
        opcao = ler_inteiro("Selecione uma opção: ")

        if opcao == 1:
            listar_produtos(estoque)
        elif opcao == 2:
            menu_cadastrar(estoque)
        elif opcao == 3:
            menu_atualizar(estoque)
        elif opcao == 4:
            menu_remover(estoque)
        elif opcao == 5:
            menu_buscar(estoque)
        elif opcao == 6:
            menu_estoque_baixo(estoque)
        elif opcao == 7:
            total = valor_total_estoque(estoque)
            print(f"\nValor total em estoque: R$ {total:.2f}")
        elif opcao == 0:
            print("\nSaindo... Até logo!")
            break
        else:
            print("\nOpção inválida.")

        pausar()


if __name__ == "__main__":
    main()
