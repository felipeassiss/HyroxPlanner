from menu import menu
from cadastro_treino import cadastro_treino
from visualizar_treino import visualizar_treino

from datetime import datetime
    

def main():
    
    while True:
        escolha = menu()

        if escolha == 1:
            cadastro_treino()
            
        elif escolha == 2:
            visualizar_treino()


main()