from datetime import datetime
from utils import limpar, pausa

competicoes = {}

def cadastrar_competicao():
    limpar()
    print("=== CADASTRAR COMPETIÇÃO ===\n")
    
    nome = input("Digite o nome da competição: ")
    data = input("Digite a data da competição (DIA/MES/ANO): ")
    
    try:
        data_formatada = datetime.strptime(data, "%d/%m/%Y").date()
    except ValueError:
        print("\nFormato de data inválido. Use DIA/MES/ANO.")
        pausa()
        return

    local = input("Digite o local da competição: ")

    competicao = {
        "nome": nome,
        "data": data_formatada,
        "local": local
    }

    competicoes[nome] = competicao

    with open("competicoes.txt", "a", encoding="utf-8") as file:
        file.write(f'{nome};{data_formatada.strftime("%d/%m/%Y")};{local}\n')

    print("\nCompetição cadastrada com sucesso!\n")
    pausa()

def visualizar_competicoes():
    limpar()
    try:
        with open("competicoes.txt", "r", encoding="utf-8") as file:
            linhas = file.readlines()

            if len(linhas) == 0:
                print("\nNenhuma competição cadastrada.\n")
                pausa()
                return

            print("=== COMPETIÇÕES CADASTRADAS ===\n")

            for linha in linhas:
                dados = linha.strip().split(";")
                if len(dados) < 3:
                    continue

                nome = dados[0]
                data_texto = dados[1]
                local = dados[2]

                data_competicao = datetime.strptime(data_texto, "%d/%m/%Y").date()
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
    
    pausa()