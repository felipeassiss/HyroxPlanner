import csv
from config import ARQUIVO
from utils import limpar, pausa, validar_texto, gerar_id

def adicionar_treino():
    limpar()
    print("=== CADASTRAR TREINO ===\n")

    nome = validar_texto(input("Nome do treino: "))
    tipo = validar_texto(input("Tipo do treino: "))
    data = validar_texto(input("Data: "))
    duracao = validar_texto(input("Duração: "))
    intensidade = validar_texto(input("Intensidade: "))

    # Loop para cadastrar múltiplos exercícios e repetições
    print("\n--- Cadastro de Exercícios ---")
    lista_exercicios = []
    while True:
        exercicio = input("Nome do exercício (ou deixe em branco para finalizar): ").strip()
        if not exercicio:
            break
        repeticoes = input(f"Quantidade de repetições para '{exercicio}': ").strip()
        lista_exercicios.append(f"{exercicio} ({repeticoes} reps)")
    
    # Junta os exercícios cadastrados em uma única string separados por " | "
    exercicios_str = " | ".join(lista_exercicios) if lista_exercicios else "Nenhum cadastrado"

    id_treino = gerar_id()

    with open(ARQUIVO, "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        
        escritor.writerow([
            id_treino, nome, tipo, data, duracao, intensidade, exercicios_str
        ])

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

                if len(linha) > 6:
                    print(f"Exercícios..: {linha[6]}")
                print("-" * 35)

            if not encontrou:
                print("Nenhum treino cadastrado.")

    except FileNotFoundError:
        print("Arquivo não encontrado.")

    pausa()

def buscar_treino():
    limpar()
    print("=== BUSCAR TREINO ===\n")

    busca = input("Digite o nome do treino: ").lower()
    encontrou = False

    try:
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
                    if len(linha) > 6:
                        print(f"Exercícios: {linha[6]}")
                    print("-" * 30)

        if not encontrou:
            print("\nTreino não encontrado.")
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
                    linha[2] = validar_texto(input("Tipo: "))
                    linha[3] = validar_texto(input("Data: "))
                    linha[4] = validar_texto(input("Duração: "))
                    linha[5] = validar_texto(input("Intensidade: "))

                    # Loop para redefinir a lista de exercícios na edição
                    print("\n--- Atualizar Exercícios ---")
                    lista_exercicios = []
                    while True:
                        exercicio = input("Nome do exercício (ou deixe em branco para finalizar): ").strip()
                        if not exercicio:
                            break
                        repeticoes = input(f"Quantidade de repetições para '{exercicio}': ").strip()
                        lista_exercicios.append(f"{exercicio} ({repeticoes} reps)")
                    
                    exercicios_str = " | ".join(lista_exercicios) if lista_exercicios else "Nenhum cadastrado"
                    
                    while len(linha) < 7:
                        linha.append("")
                    linha[6] = exercicios_str

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
            next(leitor, None) # Pula o cabeçalho

            total_treinos = 0
            tempo_total = 0
            tipos_treino = {}
            intensidades = {}

            for linha in leitor:
                if len(linha) < 6:
                    continue

                total_treinos += 1

                # Mapeia o Tipo de treino (ex: Força, Corrida)
                tipo = linha[2].strip().title()
                tipos_treino[tipo] = tipos_treino.get(tipo, 0) + 1

                # Mapeia a Intensidade
                intensidade = linha[5].strip().title()
                intensidades[intensidade] = intensidades.get(intensidade, 0) + 1

                # Tenta extrair a duração em minutos
                duracao_str = ''.join(filter(str.isdigit, linha[4]))
                if duracao_str:
                    tempo_total += int(duracao_str)

            if total_treinos == 0:
                print("Não há treinos suficientes para analisar. Vá treinar e registre no sistema!")
                pausa()
                return

            # =========================================
            # EXIBIÇÃO DOS DADOS
            # =========================================
            print(f"Total de treinos registrados: {total_treinos}")
            
            if tempo_total > 0:
                media_tempo = tempo_total // total_treinos
                print(f"Tempo total suando a camisa: {tempo_total} minutos")
                print(f"Duração média por treino: {media_tempo} minutos")

            print("\n--- Tipos de Treino Mais Frequentes ---")
            for t, qtd in sorted(tipos_treino.items(), key=lambda x: x[1], reverse=True):
                print(f"- {t}: {qtd} vezes")

            print("\n--- Perfil de Intensidade ---")
            for i, qtd in sorted(intensidades.items(), key=lambda x: x[1], reverse=True):
                print(f"- {i}: {qtd} treinos")

            # =========================================
            # IA DE RECOMENDAÇÕES BASEADA NOS DADOS
            # =========================================
            print("\n===== RECOMENDAÇÕES BASEADAS NO SEU HISTÓRICO =====")

            if total_treinos < 3:
                print("- Você está no começo! O segredo agora é consistência. Tente bater 5 treinos registrados.")
            elif total_treinos >= 10:
                print("- Volume sólido! Você já criou um bom hábito de treinos.")

            if len(tipos_treino) == 1:
                unico_tipo = list(tipos_treino.keys())[0]
                print(f"- Você está focando 100% em '{unico_tipo}'. Considere adicionar mobilidade ou cardio para equilibrar.")
            elif len(tipos_treino) >= 3:
                print("- Boa variedade de estímulos. Seu corpo não está caindo na rotina!")

            if tempo_total > 0:
                if media_tempo < 30:
                    print("- Seus treinos estão curtinhos. Se o objetivo for resistência, experimente sessões um pouco mais longas.")
                elif media_tempo > 90:
                    print("- Treinos bem longos identificados! Não esqueça que o descanso (recovery) é onde o músculo cresce.")

    except FileNotFoundError:
        print("Arquivo não encontrado. Cadastre seu primeiro treino para o sistema poder analisar!")

    pausa()