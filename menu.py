def menu(): #Função responsável por mostrar o menu
    print("=" * 40)
    print(" " * 11 + "HYROX Planner") #Criação das tabulações gráficas pelo terminal
    print("=" * 40)

    print("[1] Adicionar treino")
    print("[2] Visualizar treinos existentes") #Visualização das opções
    print("[3] Editar treino")
    print("[4] Excluir treino")
    print("[0] Sair")

    print("=" * 40)

    opcao = int(input("Escolha uma opção: "))

    return opcao