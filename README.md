# Controle de Estoque

Sistema de linha de comando (CLI), feito em Python puro, para gerenciar o estoque de uma loja de eletrônicos: cadastrar produtos, atualizar quantidades e preços, remover itens e acompanhar o que precisa ser reposto. Os dados ficam salvos em um arquivo JSON local, então as informações não se perdem entre uma execução e outra.

## Sobre o projeto

Este é um projeto acadêmico da disciplina de Python da faculdade, criado para praticar conceitos fundamentais da linguagem em um contexto prático:

- Estruturas de repetição e um menu interativo em loop
- Funções e organização de código em módulos
- Manipulação de arquivos (leitura e escrita de JSON)
- Validação de entrada do usuário
- Operações básicas de CRUD (Create, Read, Update, Delete)

## Funcionalidades

- **Listar produtos** — exibe todos os itens cadastrados em formato de tabela
- **Cadastrar produto** — adiciona um novo item (nome, quantidade e preço)
- **Atualizar produto** — edita nome, quantidade e/ou preço de um item existente
- **Remover produto** — exclui um item do estoque (com confirmação)
- **Buscar por nome** — encontra produtos a partir de parte do nome digitado
- **Relatório de estoque baixo** — lista produtos com quantidade igual ou menor que 5 unidades
- **Valor total em estoque** — soma (quantidade × preço) de todos os produtos

## Como funciona

O sistema exibe um menu numérico no terminal e repete essa exibição até que a opção **[0] Sair** seja escolhida. Cada operação de escrita (cadastrar, atualizar ou remover) salva o estoque imediatamente no arquivo `estoque.json`, então o progresso nunca depende de fechar o programa corretamente.

## Como executar

Requer apenas Python 3.8 ou superior — não há bibliotecas externas para instalar.

```bash
python controle_estoque.py
```

Na primeira execução, o arquivo `estoque.json` é criado automaticamente na mesma pasta para guardar os dados.

## Estrutura do projeto

```
Controle de Estoque/
├── controle_estoque.py   # Ponto de entrada: menu e interação com o usuário
├── estoque.py             # Camada de dados: persistência em JSON e operações de CRUD
├── utils.py                # Funções utilitárias (limpar tela, leitura validada de dados)
└── estoque.json            # Gerado automaticamente na primeira execução, não versionado
```

## Exemplo de uso

```
==========================================
  CONTROLE DE ESTOQUE - LOJA DE ELETRÔNICOS
==========================================
[1] Listar produtos
[2] Cadastrar novo produto
[3] Atualizar produto
[4] Remover produto
[5] Buscar produto por nome
[6] Relatório de estoque baixo
[7] Valor total em estoque
[0] Sair
==========================================
Selecione uma opção:
```

## Tecnologias

- Python 3 (biblioteca padrão apenas: `json`, `os`)

## Possíveis melhorias futuras

- Exportar relatórios para CSV/Excel
- Interface gráfica (Tkinter) ou web (Flask)
- Testes automatizados com `pytest`
- Controle de categorias e fornecedores

## Autor

Projeto acadêmico desenvolvido para a disciplina de Python da Faculdade.
