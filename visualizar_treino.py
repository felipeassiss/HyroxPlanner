import cadastro_treino
from tabulate import tabulate
file = open("Treinos Registrados.txt", "r", encoding= 'utf8')
def visualizar_treino(): # Função responsável pela visualização do treino
        
    if len(cadastro_treino.treinos) > 0: # Condicional que verifica se pode visualizar o treino cadastrado, caso seja maior do 0 (há pelo menos um treino), então segue o funcionamento

        print(file.read())
        file.close()

    else:

        print("\nNão há nenhum treino cadastrado!\n") # Se não houver nenhum treino ainda, informa que não há treinos

