# =========================================
# SISTEMA HYROX - IA DE SUGESTÕES
# Desenvolvedor: Breno
# =========================================

# Lista para salvar histórico
historico = []

# =========================================
# FUNÇÃO PARA CALCULAR NÍVEL
# =========================================
def calcular_nivel(pontos):

    if pontos <= 10:
        return "Iniciante"

    elif pontos <= 20:
        return "Intermediário"

    else:
        return "Avançado"


# =========================================
# FUNÇÃO DE RECOMENDAÇÕES
# =========================================
def recomendar_treino(burpees, wall_ball, sled_push, corrida):

    print("\n===== RECOMENDAÇÕES =====")

    # Resistência
    if corrida > 15:
        print("➡ Treinar resistência cardiovascular.")

    else:
        print("➡ Boa resistência cardiovascular.")

    # Explosão muscular
    if wall_ball < 20:
        print("➡ Melhorar explosão muscular.")

    else:
        print("➡ Boa explosão muscular.")

    # Força
    if sled_push < 50:
        print("➡ Aumentar treino de força.")

    else:
        print("➡ Boa força muscular.")

    # Burpees
    if burpees < 30:
        print("➡ Focar em condicionamento físico.")

    else:
        print("➡ Excelente desempenho em burpees.")

    print("===========================")


# =========================================
# FUNÇÃO PRINCIPAL DE ANÁLISE
# =========================================
def analisar_atleta():

    print("\n===== ANÁLISE DO ATLETA =====")

    nome = input("Nome do atleta: ")

    try:
        burpees = int(input("Quantidade de burpees: "))
        wall_ball = int(input("Quantidade de wall balls: "))
        sled_push = int(input("Carga do sled push (kg): "))
        corrida = float(input("Tempo da corrida (min): "))
        treinos = int(input("Treinos por semana: "))

    except ValueError:
        print("❌ ERRO: Digite apenas números válidos.")
        return

    # =========================================
    # SISTEMA DE PONTUAÇÃO
    # =========================================
    pontos = 0

    if burpees >= 30:
        pontos += 10

    if wall_ball >= 20:
        pontos += 10

    if sled_push >= 50:
        pontos += 10

    if corrida <= 15:
        pontos += 10

    if treinos >= 4:
        pontos += 10

    # =========================================
    # CALCULAR NÍVEL
    # =========================================
    nivel = calcular_nivel(pontos)

    # =========================================
    # MOSTRAR RESULTADOS
    # =========================================
    print("\n===== RESULTADO DA ANÁLISE =====")

    print(f"Atleta: {nome}")
    print(f"Pontuação: {pontos}")
    print(f"Nível: {nivel}")

    # Frequência semanal
    if treinos <= 2:
        print("➡ Sugestão: aumentar frequência semanal.")

    elif treinos <= 4:
        print("➡ Frequência de treino boa.")

    else:
        print("➡ Frequência avançada de treino.")

    # Sugestão de carga
    if nivel == "Iniciante":
        print("➡ Carga recomendada: 20kg")

    elif nivel == "Intermediário":
        print("➡ Carga recomendada: 40kg")

    else:
        print("➡ Carga recomendada: 60kg")

    # Chamar recomendações
    recomendar_treino(burpees, wall_ball, sled_push, corrida)

    # =========================================
    # SALVAR HISTÓRICO
    # =========================================
    atleta = {
        "nome": nome,
        "nivel": nivel,
        "pontos": pontos
    }

    historico.append(atleta)

    print("✅ Atleta salvo no histórico.")


# =========================================
# FUNÇÃO PARA MOSTRAR HISTÓRICO
# =========================================
def mostrar_historico():

    print("\n===== HISTÓRICO DE ATLETAS =====")

    if len(historico) == 0:
        print("Nenhum atleta cadastrado.")
        return

    for atleta in historico:

        print("----------------------------")
        print(f"Nome: {atleta['nome']}")
        print(f"Nível: {atleta['nivel']}")
        print(f"Pontuação: {atleta['pontos']}")

    print("----------------------------")


# =========================================
# MENU PRINCIPAL
# =========================================
def menu():

    while True:

        print("\n================================")
        print("      SISTEMA HYROX")
        print(" IA DE SUGESTÕES AUTOMÁTICAS")
        print("================================")

        print("1 - Analisar atleta")
        print("2 - Ver histórico")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        # =========================================
        # OPÇÃO 1
        # =========================================
        if opcao == "1":
            analisar_atleta()

        # =========================================
        # OPÇÃO 2
        # =========================================
        elif opcao == "2":
            mostrar_historico()

        # =========================================
        # OPÇÃO 3
        # =========================================
        elif opcao == "3":
            print("\nEncerrando sistema...")
            print("Obrigado por utilizar o Sistema Hyrox!")
            break

        # =========================================
        # OPÇÃO INVÁLIDA
        # =========================================
        else:
            print("❌ Opção inválida.")


# =========================================
# INICIAR SISTEMA
# =========================================
menu()