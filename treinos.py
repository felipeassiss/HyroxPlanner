import csv
import os
from datetime import datetime
from config import ARQUIVO
from utils import limpar, pausa, validar_texto, gerar_id

ARQUIVO_FUNC = "exerciciosEsp.csv"

TIPOS_TREINO = ["Corrida", "Força", "Simulado HYROX"]
NIVEIS_INTENSIDADE = ["Baixa", "Média", "Alta", "Máxima"]
EXERCICIOS_HYROX = [
    "Sled Push", "Sled Pull", "Burpee Broad Jumps", "Wall Balls",
    "Farmer's Carry", "Sandbag Lunges", "Box Push-Ups", "Rowing"
]


def _criar_arquivo_func():
    if not os.path.exists(ARQUIVO_FUNC):
        with open(ARQUIVO_FUNC, "w", encoding="utf-8") as f:
            f.write("exercicio;tempo;distancia;carga;repeticoes;data\n")


def _escolher_opcao(titulo, opcoes):
    """Exibe uma lista numerada e retorna o texto da opção escolhida."""
    while True:
        print(f"\n{titulo}")
        for i, op in enumerate(opcoes, start=1):
            print(f"{i} - {op}")
        escolha = input("Escolha uma opção: ").strip()
        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            return opcoes[int(escolha) - 1]
        print("Opção inválida. Tente novamente.")


def adicionar_treino():
    limpar()
    print("=== CADASTRAR TREINO ===\n")

    nome       = validar_texto(input("Nome do treino: "))
    tipo       = _escolher_opcao("Tipo do treino:", TIPOS_TREINO)
    data       = validar_texto(input("Data (dd/mm/aaaa): "))
    duracao    = validar_texto(input("Duração (ex: 60 minutos): "))
    intensidade = _escolher_opcao("Intensidade:", NIVEIS_INTENSIDADE)

    id_treino = gerar_id()

    with open(ARQUIVO, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([id_treino, nome, tipo, data, duracao, intensidade])

    print("\nTreino cadastrado com sucesso!")
    pausa()


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

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            cabecalho = next(leitor)
            linhas_atualizadas.append(cabecalho)

            for linha in leitor:
                if linha[0] == id_busca:
                    encontrou = True
                    print("\nDigite os novos dados:\n")

                    linha[1] = validar_texto(input("Nome: "))
                    linha[2] = _escolher_opcao("Tipo do treino:", TIPOS_TREINO)
                    linha[3] = validar_texto(input("Data (dd/mm/aaaa): "))
                    linha[4] = validar_texto(input("Duração: "))
                    linha[5] = _escolher_opcao("Intensidade:", NIVEIS_INTENSIDADE)

                linhas_atualizadas.append(linha)

        if encontrou:
            with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerows(linhas_atualizadas)
            print("\nTreino atualizado com sucesso!")
        else:
            print("\nID não encontrado.")

    except FileNotFoundError:
        print("Arquivo não encontrado.")

    pausa()


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

    try:
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

    except FileNotFoundError:
        print("Arquivo não encontrado.")

    pausa()


def analisar_historico():
    limpar()
    print("=== ANÁLISE INTELIGENTE DE TREINOS ===\n")

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor, None)

            total_treinos = 0
            tempo_total   = 0
            tipos_treino  = {}
            intensidades  = {}

            for linha in leitor:
                if len(linha) < 6:
                    continue

                total_treinos += 1

                tipo = linha[2].strip().title()
                tipos_treino[tipo] = tipos_treino.get(tipo, 0) + 1

                intensidade = linha[5].strip().title()
                intensidades[intensidade] = intensidades.get(intensidade, 0) + 1

                duracao_str = ''.join(filter(str.isdigit, linha[4]))
                if duracao_str:
                    tempo_total += int(duracao_str)

            if total_treinos == 0:
                print("Não há treinos suficientes para analisar. Vá treinar e registre no sistema!")
                pausa()
                return

            print(f"Total de treinos registrados: {total_treinos}")

            if tempo_total > 0:
                media_tempo = tempo_total // total_treinos
                print(f"Tempo total treinado: {tempo_total} minutos")
                print(f"Duração média por treino: {media_tempo} minutos")

            print("\n--- Tipos de Treino Mais Frequentes ---")
            for t, qtd in sorted(tipos_treino.items(), key=lambda x: x[1], reverse=True):
                print(f"- {t}: {qtd} vezes")

            print("\n--- Perfil de Intensidade ---")
            for i, qtd in sorted(intensidades.items(), key=lambda x: x[1], reverse=True):
                print(f"- {i}: {qtd} treinos")

            print("\n===== RECOMENDAÇÕES BASEADAS NO SEU HISTÓRICO =====")

            if total_treinos < 3:
                print("- Você está no começo! O segredo agora é consistência. Tente bater 5 treinos registrados.")
            elif total_treinos >= 10:
                print("- Volume sólido! Você já criou um bom hábito de treinos.")

            if len(tipos_treino) == 1:
                unico_tipo = list(tipos_treino.keys())[0]
                print(f"- Você está focando 100% em '{unico_tipo}'. Varie entre corrida, força e simulado HYROX.")
            elif len(tipos_treino) >= 3:
                print("- Boa variedade de estímulos. Seu corpo não está caindo na rotina!")

            if tempo_total > 0:
                if media_tempo < 30:
                    print("- Seus treinos estão curtinhos. Para HYROX, o ideal é manter sessões acima de 45 minutos.")
                elif media_tempo > 90:
                    print("- Treinos bem longos! Não esqueça que o descanso é onde o músculo se recupera.")

    except FileNotFoundError:
        print("Arquivo não encontrado. Cadastre seu primeiro treino para o sistema poder analisar!")

    pausa()


def cadastrar_exercicio():
    limpar()
    print("=== CADASTRAR EXERCÍCIO HYROX ===\n")

    exercicio = _escolher_opcao("Exercício:", EXERCICIOS_HYROX)

    try:
        tempo      = float(input("Tempo (minutos): "))
        distancia  = float(input("Distância percorrida (metros): "))
        carga      = float(input("Carga utilizada (kg): "))
        repeticoes = int(input("Quantidade de repetições: "))
    except ValueError:
        print("\nERRO: Digite valores numéricos válidos.")
        pausa()
        return

    data = datetime.now().strftime("%d/%m/%Y")

    with open(ARQUIVO_FUNC, "a", encoding="utf-8") as f:
        f.write(f"{exercicio};{tempo};{distancia};{carga};{repeticoes};{data}\n")

    print("\nExercício cadastrado com sucesso!")
    pausa()


def listar_exercicios():
    limpar()
    print("=== LISTA DE EXERCÍCIOS ===\n")

    try:
        with open(ARQUIVO_FUNC, "r", encoding="utf-8") as f:
            linhas = f.readlines()

        if len(linhas) <= 1:
            print("Nenhum exercício cadastrado.")
            pausa()
            return

        for i, linha in enumerate(linhas[1:], start=1):
            dados = linha.strip().split(";")
            print(f"REGISTRO {i}")
            print(f"Exercício  : {dados[0]}")
            print(f"Tempo      : {dados[1]} minutos")
            print(f"Distância  : {dados[2]} metros")
            print(f"Carga      : {dados[3]} kg")
            print(f"Repetições : {dados[4]}")
            print(f"Data       : {dados[5]}")
            print("-" * 35)

    except FileNotFoundError:
        print("Arquivo não encontrado.")

    pausa()


def evolucao_atleta():
    limpar()
    print("=== EVOLUÇÃO DO ATLETA ===\n")

    exercicio_busca = _escolher_opcao("Selecione o exercício:", EXERCICIOS_HYROX)

    cargas           = []
    repeticoes_lista = []
    tempos           = []
    distancias       = []

    try:
        with open(ARQUIVO_FUNC, "r", encoding="utf-8") as f:
            linhas = f.readlines()[1:]

        for linha in linhas:
            dados = linha.strip().split(";")
            if dados[0].lower() == exercicio_busca.lower():
                tempos.append(float(dados[1]))
                distancias.append(float(dados[2]))
                cargas.append(float(dados[3]))
                repeticoes_lista.append(int(dados[4]))

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        pausa()
        return

    if not cargas:
        print(f"\nNenhum registro encontrado para '{exercicio_busca}'.")
        pausa()
        return

    print(f"\nRESULTADO: {exercicio_busca}")
    print(f"Registros encontrados : {len(cargas)}")
    print(f"Maior carga           : {max(cargas)} kg")
    print(f"Menor carga           : {min(cargas)} kg")
    print(f"Média de repetições   : {sum(repeticoes_lista) / len(repeticoes_lista):.1f}")
    print(f"Melhor tempo          : {min(tempos)} minutos")
    print(f"Maior distância       : {max(distancias)} metros")

    pausa()


def menu_treinos():
    while True:
        limpar()
        print("=== CRUD DE TREINOS ===\n")
        print("1 - Cadastrar treino")
        print("2 - Listar treinos")
        print("3 - Editar treino")
        print("4 - Excluir treino")
        print("5 - Análise inteligente")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if   opcao == "1": adicionar_treino()
        elif opcao == "2": listar_treinos()
        elif opcao == "3": editar_treino()
        elif opcao == "4": excluir_treino()
        elif opcao == "5": analisar_historico()
        elif opcao == "0": break
        else:
            print("\nOpção inválida.")
            pausa()


def menu_exercicios():
    _criar_arquivo_func()

    while True:
        limpar()
        print("=== EXERCÍCIOS HYROX ===\n")
        print("1 - Cadastrar exercício")
        print("2 - Listar exercícios")
        print("3 - Evolução do atleta")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if   opcao == "1": cadastrar_exercicio()
        elif opcao == "2": listar_exercicios()
        elif opcao == "3": evolucao_atleta()
        elif opcao == "0": break
        else:
            print("\nOpção inválida.")
            pausa()


def menu_principal():
    while True:
        limpar()
        print("=== HYROX PLANNER ===\n")
        print("1 - Treinos")
        print("2 - Exercícios HYROX")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if   opcao == "1": menu_treinos()
        elif opcao == "2": menu_exercicios()
        elif opcao == "0": break
        else:
            print("\nOpção inválida.")
            pausa()
