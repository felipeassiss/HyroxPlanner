from menu import menu
from cadastro_treino import cadastro_treino
from visualizar_treino import visualizar_treino
from editar_treino import editar_treino
from excluir_treino import excluir_treino

from datetime import datetime
    

def main():
    
    while True:
        escolha = menu()

        if escolha == 1:
            cadastro_treino()
            
        elif escolha == 2:
            visualizar_treino()
        
        elif escolha == 3:
            editar_treino()
        
        elif escolha == 4:
            excluir_treino()
            


main()