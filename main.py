# HYROX PLANNER - CRUD

import csv
import os

ARQUIVO = "treinos.csv"


# Criar arquivo
def criar_arquivo():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([
                "ID",
                "Nome",
                "Tipo",
                "Data",
                "Duracao",
                "Intensidade"
            ])


# Limpar terminal
def limpar():
    os.system("cls" if os.name == "nt" else "clear")


# Pausa
def pausa():
    input("\nENTER para continuar...")


# Gerar ID
def gerar_id():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            linhas = list(csv.reader(arquivo))

            if len(linhas) <= 1:
                return 1

            ultimo_id = int(linhas[-1][0])
            return ultimo_id + 1

    except:
        return 1


# Validar texto
def validar_texto(texto):
    while texto.strip() == "":
        texto = input("Campo vazio. Digite novamente: ")
    return texto


# Cadastrar treino
def adicionar_treino():
    limpar()
    print("=== CADASTRAR TREINO ===\n")

    nome = validar_texto(input("Nome do treino: "))
    tipo = validar_texto(input("Tipo do treino: "))
    data = validar_texto(input("Data: "))
    duracao = validar_texto(input("Duração: "))
    intensidade = validar_texto(input("Intensidade: "))

    id_treino = gerar_id()

    with open(ARQUIVO, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([
            id_treino,
            nome,
            tipo,
            data,
            duracao,
            intensidade
        ])

    print("\nTreino cadastrado com sucesso!")
    pausa()


# Listar treinos
def listar_treinos():
    limpar()
    print("=== LISTA DE TREINOS ===\n")

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)

            encontrou = False

            for linha in leitor:
                encontrou = True
                print(f"ID..........: {linha[0]}")
                print(f"Nome........: {linha[1]}")
                print(f"Tipo........: {linha[2]}")
                print(f"Data........: {linha[3]}")
                print(f"Duração.....: {linha[4]}")
                print(f"Intensidade.: {linha[5]}")
                print("-" * 35)

            if not encontrou:
                print("Nenhum treino cadastrado.")

    except FileNotFoundError:
        print("Arquivo não encontrado.")

    pausa()


# Buscar treino
def buscar_treino():
    limpar()
    print("=== BUSCAR TREINO ===\n")

    busca = input("Digite o nome do treino: ").lower()
    encontrou = False

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)

        for linha in leitor:
            if busca in linha[1].lower():
                encontrou = True
                print(f"\nID: {linha[0]}")
                print(f"Nome: {linha[1]}")
                print(f"Tipo: {linha[2]}")
                print(f"Data: {linha[3]}")
                print(f"Duração: {linha[4]}")
                print(f"Intensidade: {linha[5]}")
                print("-" * 30)

    if not encontrou:
        print("\nTreino não encontrado.")

    pausa()


# Editar treino
def editar_treino():
    limpar()
    print("=== EDITAR TREINO ===\n")

    id_busca = input("Digite o ID do treino: ")

    if not id_busca.isdigit():
        print("\nDigite apenas números.")
        pausa()
        return

    linhas_atualizadas = []
    encontrou = False

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        cabecalho = next(leitor)
        linhas_atualizadas.append(cabecalho)

        for linha in leitor:
            if linha[0] == id_busca:
                encontrou = True
                print("\nDigite os novos dados:\n")

                linha[1] = validar_texto(input("Nome: "))
                linha[2] = validar_texto(input("Tipo: "))
                linha[3] = validar_texto(input("Data: "))
                linha[4] = validar_texto(input("Duração: "))
                linha[5] = validar_texto(input("Intensidade: "))

            linhas_atualizadas.append(linha)

    if encontrou:
        with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(linhas_atualizadas)

        print("\nTreino atualizado com sucesso!")
    else:
        print("\nID não encontrado.")

    pausa()


# Excluir treino
def excluir_treino():
    limpar()
    print("=== EXCLUIR TREINO ===\n")

    id_busca = input("Digite o ID do treino: ")

    if not id_busca.isdigit():
        print("\nDigite apenas números.")
        pausa()
        return

    confirmar = input("Tem certeza? (s/n): ").lower()

    if confirmar != "s":
        print("\nExclusão cancelada.")
        pausa()
        return

    linhas_atualizadas = []
    encontrou = False

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        cabecalho = next(leitor)
        linhas_atualizadas.append(cabecalho)

        for linha in leitor:
            if linha[0] == id_busca:
                encontrou = True
            else:
                linhas_atualizadas.append(linha)

    if encontrou:
        with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(linhas_atualizadas)

        print("\nTreino excluído com sucesso!")
    else:
        print("\nID não encontrado.")

    pausa()


# Menu
def menu():
    criar_arquivo()

    while True:
        limpar()

        print("======== HYROX PLANNER ========")
        print("1 - Cadastrar treino")
        print("2 - Listar treinos")
        print("3 - Buscar treino")
        print("4 - Editar treino")
        print("5 - Excluir treino")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_treino()
        elif opcao == "2":
            listar_treinos()
        elif opcao == "3":
            buscar_treino()
        elif opcao == "4":
            editar_treino()
        elif opcao == "5":
            excluir_treino()
        elif opcao == "0":
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOpção inválida.")
            pausa()


# Iniciar
menu()
