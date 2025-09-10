#### Projetinho 1: Gerenciador de Biblioteca
# Os alunos vão criar um sistema que permite que uma biblioteca gerencie seus livros. 
# Eles poderão adicionar livros, listar todos os livros disponíveis e buscar um livro pelo título. 
# Vamos estruturar o projeto da seguinte maneira:

# - **Adicionar Livro**: O usuário pode adicionar um novo livro, que inclui título e autor.
# - **Listar Livros**: O sistema deve mostrar todos os livros que estão na biblioteca.
# - **Buscar Livro**: O usuário pode buscar um livro pelo título e o sistema deve retornar informações sobre o livro, se ele estiver disponível.


def adicionar_livro(livros, titulo, autor):
    """Adiciona um livro à lista de livros."""
    livro = {'titulo': titulo, 'autor': autor}
    livros.append(livro)
    print(f'Livro "{titulo}" adicionado com sucesso!')

def listar_livros(livros):
    """Lista todos os livros disponíveis na biblioteca."""
    if not livros:
        print("Nenhum livro disponível.")
    else:
        print("Livros disponíveis:")
        for livro in livros:
            print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]}')

def buscar_livro(livros, titulo):
    """Busca um livro pelo título."""
    for livro in livros:
        if livro['titulo'].lower() == titulo.lower():
            print(f'Livro encontrado: Título: {livro["titulo"]}, Autor: {livro["autor"]}')
            return
    print(f'Livro "{titulo}" não encontrado.')

def buscar_autor(livros, autor):
    """Busca um livro pelo autor."""
    for livro in livros:
        if livro['autor'].lower() == autor.lower():
            print(f'Livro encontrado: Título: {livro["titulo"]}, Autor: {livro["autor"]}')
            return
    print(f'Autor "{autor}" não encontrado.')

def menu():
    """Exibe o menu e lida com as opções do usuário."""
    # Lista para armazenar os livros
    livros = []
    while True:
        print("\nMenu:")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Buscar Livro")
        print("4. Buscar Autor")
        print("0. Sair")

        escolha = input("Escolha uma opção (1-4): ")
        match escolha:
            case '1':
                titulo = input("Digite o título do livro: ")
                autor = input("Digite o autor do livro: ")
                adicionar_livro(livros, titulo, autor)
            case '2':
                listar_livros(livros)
            case '3':
                titulo = input("Digite o título do livro que deseja buscar: ")
                buscar_livro(livros, titulo)
            case '4':
                autor = input("Digite o autor do livro que deseja buscar: ")
                buscar_autor(livros, autor)
            case '0':
                print("Saindo do programa...")
                break
            case _:
                print("Opção inválida. Por favor, escolha novamente.")

menu()
