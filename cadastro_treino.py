from datetime import datetime, timedelta

treinos = {}

def cadastro_treino():   
    nome = input("Digite o nome do treino: ")

    tipo = input("Tipo do treino (corrida, força, simulado): ")

    data = input("Data do treino (DIA/MES/ANO): ")
    data_formatada = datetime.strptime(data, "%d/%m/%Y").date()

    duracao = input("Duração do treino (HORAS:MINUTOS:SEGUNDOS): ")
    horas, minutos, segundos = map(int, duracao.split(":"))
    duracao_formatada = timedelta(hours=horas, minutes=minutos, seconds=segundos)

    intensidade = input("Intensidade do treino: (leve, médio, pesado): ")

    treino = {
        "nome": nome,
        "tipo": tipo,
        "data": data_formatada,
        "duracao": duracao_formatada,
        "intensidade": intensidade
    }

    treinos[nome] = treino

    print("Treino cadastrado com sucesso!")