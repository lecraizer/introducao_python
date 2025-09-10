receitas = []

def adicionar_receita():
    '''
    Função para adicionar uma receita à lista de receitas
    '''
    nome = input("Digite o nome da receita: ")
    ingredientes = input("Digite os ingredientes separados por vírgula: ")
    categoria = input("Digite a categoria (ex: sobremesa, prato principal): ")
    receita = {
        "nome": nome,
        "ingredientes": ingredientes.split(', '),
        "categoria": categoria
    }
    receitas.append(receita)
    print(f"\nReceita {receita['nome']} adicionada com sucesso!\n")


def listar_receitas():
    if not receitas:
        print('Nenhuma receita cadastrada')
        return
    print("\n=== Lista de receitas ===")
    for i, receita in enumerate(receitas, 1):
        print(f"{i}. {receita['nome']} ({len(receita['ingredientes'])} ingredientes) - {receita['categoria']}")
    print('\n')


def todas_tem_ingrediente():
    ingrediente = input("Digite o ingrediente para buscar: ")
    resultado = all(ingrediente in receita['ingredientes'] for receita in receitas)
    print(f"Todas as receitas possuem {ingrediente}? {'Sim' if resultado else 'Não'}")


def alguma_tem_ingrediente():
    ingrediente = input("Digite o ingrediente para buscar: ")
    resultado = any(ingrediente in receita['ingredientes'] for receita in receitas)
    # if resultado:
    #     print('Sim')
    # else:
    #     print('Não')
    print(f"Alguma receita contém {ingrediente}? {'Sim' if resultado else 'Não'}")


def filtrar_por_categoria():
    categoria = input("Digite a categoria para filtrar (ex.: sobremesa, prato principal): ")
    receitas_filtradas = list(filter(lambda r: r['categoria'] == categoria, receitas)) # resultado vai ser uma lista com as receitas cujas categorias seja iguais à digitada
    if not receitas_filtradas:
        print('Nenhuma receita foi encontrada')
    else:
        print(receitas_filtradas)


def ordernar_receitas():
    opcao = input("Escolha entre ordenar por nome (1) ou ordenar por qte de ingredientes (2)")
    if opcao == "1":
        receitas_ordenadas = sorted(receitas, key=lambda x: x['nome'])
    elif opcao == "2":
        receitas_ordenadas = sorted(receitas, key=lambda x: len(x['ingredientes']), reverse=True)
    else:
        print("Opção inválida! Escolha entre (1) ou (2)")
    
    print(receitas_ordenadas, '\n')


def transformar_nomes_maisculos():
    if len(receitas) == 0:
        print('Nenhuma receita cadastrada')
        return
    
    nomes_maiusculos = list(map(lambda r: r['nome'].upper(), receitas))
    print(nomes_maiusculos)
       

def menu():
    while True:
        print('\n===Sistema de gerenciamento de receitas===')
        print('1. Adicionar receita')
        print('2. Listas todas as receitas')
        print('3. Verificar se todas as receitas possuem um ingrediente específico')
        print('4. Verificar se alguma receita contém um ingrediente específico')
        print('5. Filtrar receitas por alguma categoria específica')
        print('6. Ordenar receitas')
        print('7. Transformar nomes de receitas para maiúsculas')
        print('8. Sair do programa')

        opcao = input('Escolha uma opção: ')
        
        match opcao:
            case '1':
                adicionar_receita()
            case '2':
                listar_receitas()
            case '3':
                todas_tem_ingrediente()
            case '4':
                alguma_tem_ingrediente()
            case '5':
                filtrar_por_categoria()
            case '6':
                ordernar_receitas()
            case '7':
                transformar_nomes_maisculos()
            case '8':
                print('Até logo!')
                break
            case _:
                print("Opção inválida! Tente novamente.")
           
if __name__ == "__main__":
    menu()
        
    