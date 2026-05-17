from datetime import datetime, timedelta
file = open("Treinos Registrados.txt", "a", encoding= 'utf8')
treinos = {}

def cadastro_treino():   
    nome = input("Digite o nome do treino: ")

    tipo = input("Tipo do treino (corrida, força, simulado): ")

    data = input("Data do treino (DIA/MES/ANO): ")
    data_formatada = datetime.strptime(data, "%d/%m/%Y").date()

    qtd_exercicio = int(input("Digite a quantidade de exercicios que foram feitos: "))

    exercicios = [] #criando uma lista vazia para armazenar os exercícios, onde cada exercício é um dicionário com nome e repetições
    for i in range(qtd_exercicio): # 'for' que solicita ao usuário quantos foram feitos com seus respectivos nomes e repetições

        nome_exercicio = input("Digite o nome do exercicio: ")
        repeticoes = int(input("Digite a quantidade de repetições que foram realizadas: "))

        exercicio = {
            "nome" : nome_exercicio,
            "repeticoes" : repeticoes
        }
        exercicios.append(exercicio)

    duracao = input("Duração do treino (HORAS:MINUTOS:SEGUNDOS): ")
    horas, minutos, segundos = map(int, duracao.split(":"))
    duracao_formatada = timedelta(hours=horas, minutes=minutos, seconds=segundos)
    intensidade = input("Intensidade do treino: (leve, médio, pesado): ")

    treino = {
        "nome": nome,
        "tipo": tipo,
        "exercicios" : exercicios,
        "data": data_formatada,
        "duracao": duracao_formatada,
        "intensidade": intensidade
    }

    treinos[nome] = treino
    file.writelines(f"{treinos}"'\n')
    file.close()
    print("Treino cadastrado com sucesso!")
