'''

Projetinho 0 - Mini-editor de Texto

Implemente um programa simples de gerenciamento de texto com as seguintes funcionalidades:
1. Adicionar frase ao final do texto.
2. Substituir palavra por outra (todas as ocorrências, sem diferenciar maiúsculas/minúsculas).
3. Censurar palavra: substituir todas as ocorrências de uma palavra por ***.

Observações:

- A variável texto começa vazia ("").
- Como strings são imutáveis, todas as funções devem retornar a nova versão do texto.
- O menu roda em loop até o usuário escolher 0 - Sair.

'''

def adicionar_frase(texto, frase):
    """Adiciona uma frase ao final do texto, separada por espaço."""
    if not texto:
        return frase
    return texto + " " + frase

def substituir_palavra(texto, alvo, novo):
    """Substitui todas as ocorrências de uma palavra pelo novo valor."""
    return texto.replace(alvo, novo)

def censurar_palavra(texto, palavra):
    """Substitui todas as ocorrências da palavra por ***."""
    return texto.replace(palavra, "***")

def mostrar_menu():
    print("\n==== Mini-editor de Texto ====")
    print("1) Adicionar frase")
    print("2) Substituir palavra")
    print("3) Censurar palavra")
    print("4) Mostrar texto")
    print("0) Sair")

def main():
    texto = ""

    while True:
        mostrar_menu()
        opcao = input("Escolha: ")

        match opcao:
            case "1":
                frase = input("Digite a frase: ")
                texto = adicionar_frase(texto, frase)
                print("Frase adicionada!")

            case "2":
                alvo = input("Palavra a substituir: ")
                novo = input("Substituir por: ")
                texto = substituir_palavra(texto, alvo, novo)
                print("Substituição feita!")

            case "3":
                palavra = input("Palavra a censurar: ")
                texto = censurar_palavra(texto, palavra)
                print("Palavra censurada!")

            case "4":
                print("\n--- TEXTO ATUAL ---")
                print(texto if texto else "(vazio)")
                print("-------------------")

            case "0":
                print("Até mais!")
                break

            case _:
                print("Opção inválida!")

if __name__ == "__main__":
    main()
