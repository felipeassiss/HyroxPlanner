import cadastro_treino

def visualizar_treino(): # Função responsável pela visualização do treino: caso exista um treino, ou seja, o tamanho da lista em que estão salvas as informações do treino é maior
                        # do que 0, exibe todo o conteúdo do cadastro. Caso contrário, mostra uma mensagem inválidando a escolha do usuário, visto que não há treinos cadastrados.
        
    if len(cadastro_treino.treinos) > 0:

        for treino_registro in cadastro_treino.treinos:

            print("Nome:", treino_registro["nome"])
            print("Tipo:", treino_registro["tipo"])
            print("Data:", treino_registro["data"])
            print("Duracao:", treino_registro["duracao"])
            print("Intensidade:", treino_registro["intensidade"])

    else:
        print("Não há nenhum treino cadastrado!")

