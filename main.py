from menu import menu
from cadastro_treino import cadastro_treino
from visualizar_treino import visualizar_treino
from editar_treino import editar_treino
from excluir_treino import excluir_treino
from competicoes import cadastrar_competicao
from competicoes import visualizar_competicoes
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

        elif escolha == 5:
            cadastrar_competicao()
        
        elif escolha == 6:
            visualizar_competicoes()
            
        elif escolha == 0:
            print("Encerrando HYROX Planner...")
            break
            
        else:
            print("Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    main()