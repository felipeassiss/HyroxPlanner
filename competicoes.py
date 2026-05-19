import os 
os.system("cls")

from datetime import datetime

competicoes = {}


def cadastrar_competicao():

    nome = input("Digite o nome da competição: ")

    data = input("Digite a data da competição (DIA/MES/ANO): ")

    data_formatada = datetime.strptime(data, "%d/%m/%Y").date()

    local = input("Digite o local da competição: ")

    competicao = {
        "nome": nome,
        "data": data_formatada,
        "local": local
    }

    competicoes[nome] = competicao

    with open("competicoes.txt", "a", encoding="utf-8") as file:

        file.write(
            f'{nome};{data_formatada.strftime("%d/%m/%Y")};{local}\n'
        )

    print("\nCompetição cadastrada com sucesso!\n")


def visualizar_competicoes():

    try:

        with open("competicoes.txt", "r", encoding="utf-8") as file:

            linhas = file.readlines()

            if len(linhas) == 0:
                print("\nNenhuma competição cadastrada.\n")
                return

            print("\n=== COMPETIÇÕES CADASTRADAS ===\n")

            for linha in linhas:

                dados = linha.strip().split(";")

                nome = dados[0]
                data_texto = dados[1]
                local = dados[2]

                data_competicao = datetime.strptime(
                    data_texto,
                    "%d/%m/%Y"
                ).date()

                hoje = datetime.now().date()

                dias_faltando = (data_competicao - hoje).days

                print(f"Competição: {nome}")
                print(f"Local: {local}")
                print(f"Data: {data_texto}")

                if dias_faltando > 0:
                    print(f"Faltam {dias_faltando} dias")
                
                elif dias_faltando == 0:
                    print("A competição é hoje!")
                
                else:
                    print("Competição já aconteceu!")

                print("-" * 30)

    except FileNotFoundError:

        print("\nArquivo de competições não encontrado.\n")
 