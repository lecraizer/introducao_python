### Projetinho 2: Gerenciador de Inventário

# Neste projeto, você irá criar um sistema de gerenciamento de inventário que permitirá adicionar, listar, buscar, remover e atualizar produtos, além de verificar quais produtos estão esgotados e calcular o valor total do estoque. O projeto será estruturado da seguinte maneira:

## Funcionalidades

# - **Adicionar Produto**: Permite que o usuário adicione um novo produto ao inventário, incluindo nome, quantidade e preço.
# - **Listar Produtos**: Exibe todos os produtos atualmente no inventário.
# - **Buscar Produto**: Permite que o usuário busque um produto pelo nome e veja suas informações se ele estiver disponível.
# - **Remover Produto**: Remove um produto específico do inventário.
# - **Atualizar Estoque**: Atualiza a quantidade de um produto existente no inventário.
# - **Mostrar Produtos Esgotados**: Lista os produtos que estão com quantidade igual a zero.
# - **Calcular Valor Total em Estoque**: Calcula e exibe o valor total de todos os produtos em estoque.
# - **Sair**: Encerra o programa.

## Estrutura do Projeto

# O projeto deverá incluir uma função `main()` que serve como ponto de entrada do programa e gerencia a interação com o usuário. A `main()` chamará as funções auxiliares de acordo com a opção escolhida pelo usuário.

### Exemplo de Fluxo de Uso

# 1. O usuário inicia o programa e vê um menu com as opções disponíveis.
# 2. O usuário escolhe adicionar um produto e insere as informações necessárias.
# 3. O usuário pode listar todos os produtos para ver os itens no inventário.
# 4. O usuário pode buscar, remover, atualizar, ou realizar outras ações conforme desejar.
# 5. O programa permanece em execução até que o usuário escolha a opção de sair.

### Estrutura de Código Sugerida

# - **Função `adicionar_produto`**: Adiciona um dicionário representando um produto à lista de inventário.
# - **Função `listar_produtos`**: Exibe todos os produtos da lista.
# - **Função `buscar_produto`**: Busca um produto pelo nome e exibe suas informações, se encontrado.
# - **Função `remover_produto`**: Remove um produto da lista com base no nome.
# - **Função `atualizar_estoque`**: Atualiza a quantidade de um produto específico.
# - **Função `mostrar_produtos_esgotados`**: Mostra produtos que estão esgotados.
# - **Função `calcular_valor_total`**: Calcula o valor total do inventário.
# - **Função `main()`**: Recebe a entrada do usuário e chama as funções apropriadas com base na escolha.

# Use esse enunciado como guia para o desenvolvimento do projeto em Python e para orientar a implementação da função `main()` que irá controlar o fluxo do programa.


# Funções para o gerenciador de inventário

def adicionar_produto(inventario, nome, quantidade, preco):
    inventario.append({'nome': nome, 'quantidade': quantidade, 'preco': preco})
    print(f"Produto '{nome}' adicionado com sucesso!")

def listar_produtos(inventario):
    if not inventario:
        print("O inventário está vazio.")
    else:
        print("Produtos no inventário:")
        for produto in inventario:
            print(f"Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R${produto['preco']:.2f}")

def buscar_produto(inventario, nome):
    for produto in inventario:
        if produto['nome'].lower() == nome.lower():
            print(f"Produto encontrado: Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R${produto['preco']:.2f}")
            return
    print(f"Produto '{nome}' não encontrado.")

def remover_produto(inventario, nome):
    for produto in inventario:
        if produto['nome'].lower() == nome.lower():
            inventario.remove(produto)
            print(f"Produto '{nome}' removido com sucesso!")
            return
    print(f"Produto '{nome}' não encontrado.")

def atualizar_estoque(inventario, nome, nova_quantidade):
    for produto in inventario:
        if produto['nome'].lower() == nome.lower():
            produto['quantidade'] = nova_quantidade
            print(f"Quantidade do produto '{nome}' atualizada para {nova_quantidade}.")
            return
    print(f"Produto '{nome}' não encontrado.")

def mostrar_produtos_esgotados(inventario):
    esgotados = [produto for produto in inventario if produto['quantidade'] == 0]
    if not esgotados:
        print("Nenhum produto esgotado.")
    else:
        print("Produtos esgotados:")
        for produto in esgotados:
            print(f"Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")

def calcular_valor_total(inventario):
    total = sum(produto['quantidade'] * produto['preco'] for produto in inventario)
    print(f"Valor total em estoque: R${total:.2f}")

# Função principal para gerenciar o fluxo do programa
def main():
    inventario = []
    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar Produto")
        print("2 - Listar Produtos")
        print("3 - Buscar Produto")
        print("4 - Remover Produto")
        print("5 - Atualizar Estoque")
        print("6 - Mostrar Produtos Esgotados")
        print("7 - Calcular Valor Total em Estoque")
        print("8 - Sair")

        opcao = input("Digite o número da opção desejada: ")

        match opcao:
            case '1':
                nome = input("Digite o nome do produto: ")
                quantidade = int(input("Digite a quantidade: "))
                preco = float(input("Digite o preço: "))
                adicionar_produto(inventario, nome, quantidade, preco)
            case '2':
                listar_produtos(inventario)
            case '3':
                nome = input("Digite o nome do produto para buscar: ")
                buscar_produto(inventario, nome)
            case '4':
                nome = input("Digite o nome do produto para remover: ")
                remover_produto(inventario, nome)
            case '5':
                nome = input("Digite o nome do produto para atualizar: ")
                nova_quantidade = int(input("Digite a nova quantidade: "))
                atualizar_estoque(inventario, nome, nova_quantidade)
            case '6':
                mostrar_produtos_esgotados(inventario)
            case '7':
                calcular_valor_total(inventario)
            case '8':
                print("Saindo do programa...")
                break
            case _:
                print("Opção inválida. Tente novamente.")
                continue
main()
