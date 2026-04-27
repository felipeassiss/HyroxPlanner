import cadastro_treino

def excluir_treino():

    if len(cadastro_treino.treinos) > 0:

        for nome_treino in cadastro_treino.treinos:
            
            print(nome_treino)


        nome_treino = input("Digite o nome do treino que deseja excluir: ")


        if nome_treino in cadastro_treino.treinos:
            del cadastro_treino.treinos[nome_treino]
            print(f"\n Treino '{nome_treino}' excluído com sucesso!\n")
            
        else:
            print("\nNome de treino inválido ou não cadastrado.\n")
    
    else:
        print("\n Não é possível excluir treinos pois não há nenhum treino cadastrado. \n")