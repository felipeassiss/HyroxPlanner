import cadastro_treino
from tabulate import tabulate

def visualizar_treino(): # Função responsável pela visualização do treino
        
    if len(cadastro_treino.treinos) > 0: # Condicional que verifica se pode visualizar o treino cadastrado, caso seja maior do 0 (há pelo menos um treino), então segue o funcionamento

        for nome_treino in cadastro_treino.treinos: # Exibe os nomes dos treinos cadastrados

            print(nome_treino)
        
        nome_treino = input("Digite o treino que deseja visualizar: ") # Pergunta ao usuário qual treino ele deseja visualizar com detalhes

        if nome_treino in cadastro_treino.treinos: # Caso o nome do treino esteja nos cadastrados, exibe as informações atreladas a ele

            treino_registro = cadastro_treino.treinos[nome_treino]

            exercicios_texto = " "


            for exercicio in treino_registro["exercicios"]:
                exercicios_texto += f'{exercicio["nome"]} - {exercicio["repeticoes"]} repetições \n'

            data = [ ["Nome", treino_registro["nome"]], 
                    ["Tipo", treino_registro["tipo"]],
                    ["Exercícios", treino_registro["exercicios"]],
                    ["Data", treino_registro["data"].strftime("%d/%m/%Y")], 
                    ["Duracao", treino_registro["duracao"]], 
                    ["Intensidade", treino_registro["intensidade"]]]
            
            print(tabulate(data, headers=["Atributo", "Descrição"], tablefmt="grid")) # Exibe as informações do treino em formato de tabela, utilizando a biblioteca tabulate
        
        else:
            print(("\nTreino não encontrado.\n")) # Caso contrário, mostra mensagem informando que não há treino com esse nome

    else:

        print("\nNão há nenhum treino cadastrado!\n") # Se não houver nenhum treino ainda, informa que não há treinos

