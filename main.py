from datetime import datetime


def menu():
    print("\t \t MENU HYROX Planner \t \t \t")
    
    opcao = int(input(
            ("Escolha uma opção: \n"
            "1-adicionar treino \n"
            "2-visualizar treinos existentes \n"
            "3-editar treinos \n"
            "4-excluir treinos \n")))
    

def cadastro_treino():
    nome = input("Digite o nome do treino: ")
    tipo = input("Digite o tipo do treino (corrida, força, simulado): ")
    data = input("Digite a data do treino (DIA/MES/ANO)")
    data = datetime.strptime(data, "%d/%m/%Y")
    