import os
from datetime import datetime

ARQUIVO = "exerciciosEsp.csv"


def criar_arquivo():

    if not os.path.exists(ARQUIVO):

        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:

            arquivo.write(
                "exercicio;tempo;distancia;carga;repeticoes;data\n"
            )


def cadastrar_exercicio():

    print("\n\n CADASTRAR EXERCÍCIO \n ")

    exercicio = input("Nome do exercício : ")

    try:

        tempo = input("Tempo (minutos): ")

        distancia = float(input("Distância percorrida (metros): "))

        carga = float(input("Carga utilizada (kg): "))

        repeticoes = int(input("Quantidade de repetições: "))

    except ValueError:

        print("\nERRO: Digite valores válidos.")
        return

    data = datetime.now().strftime("%d/%m/%Y")

    with open(ARQUIVO, "a", encoding="utf-8") as arquivo:

        arquivo.write(
            f"{exercicio};"
            f"{tempo};"
            f"{distancia};"
            f"{carga};"
            f"{repeticoes};"
            f"{data}\n"
        )

    print("\nExercício cadastrado com sucesso!")


def listar_exercicios():

    print("\n\n LISTA DE EXERCÍCIOS \n ")

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

        linhas = arquivo.readlines()

        if len(linhas) <= 1:

            print("Nenhum exercício cadastrado.")
            return

        for i, linha in enumerate(linhas[1:], start=1):

            dados = linha.strip().split(";")

            print(f"REGISTRO {i}\nExercício : {dados[0]}\nTempo: {dados[1]} minutos\nDistância: {dados[2]} metros\nCarga: {dados[3]} kg\nRepetições: {dados[4]} repetições\nData: {dados[5]}\n")


def mostrar_evolucao():

    print("\n\n EVOLUÇÃO DO ATLETA \n ")

    exercicio_busca = input("Digite o nome do exercício: ")

    cargas = []
    repeticoes_lista = []

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:

        linhas = arquivo.readlines()[1:]

        for linha in linhas:

            dados = linha.strip().split(";")

            nome = dados[0]

            if nome.lower() == exercicio_busca.lower():

                cargas.append(float(dados[3]))
                repeticoes_lista.append(int(dados[4]))

    if len(cargas) == 0:

        print("\nExercício não encontrado.")
        return

    print(f"\nRESULTADO: {exercicio_busca} ")

    print(f"Maior carga registrada: {max(cargas)} kg")
    print(f"Menor carga registrada: {min(cargas)} kg")

    media = sum(repeticoes_lista) / len(repeticoes_lista)

    print(f"Média de repetições: {media:.1f}\n")


def menu_exer_funcionais():

    criar_arquivo()

    while True:

        print("\n\nEXERCÍCIOS HYROX\n\n1 - Cadastrar exercício\n2 - Listar exercícios\n3 - Mostrar evolução\n4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            cadastrar_exercicio()

        elif opcao == "2":

            listar_exercicios()

        elif opcao == "3":

            mostrar_evolucao()

        elif opcao == "4":

            print("\nSaindo...")
            break

        else:

            print("\nOpção inválida.")


menu_exer_funcionais()
