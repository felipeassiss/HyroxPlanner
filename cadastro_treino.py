from datetime import datetime

treinos = []

def cadastro_treino():

    nome = input("Digite o nome do treino: ")

    tipo = input("Tipo do treino (corrida, força, simulado): ")

    data = input("Data do treino (DIA/MES/ANO): ")
    data_formatada = datetime.strptime(data, "%d/%m/%Y")

    duracao = input("Duração do treino (HORAS:MINUTOS:SEGUNDOS): ")
    duracao_formatada = datetime.strptime(duracao, "%H:%M:%S")

    intensidade = input("Intensidade do treino: (leve, médio, pesado): ")


    treino = {
        "nome" : nome,
        "tipo" : tipo,
        "data" : data_formatada,
        "duracao" : duracao_formatada,
        "intensidade" : intensidade
    }

    treinos.append(treino)