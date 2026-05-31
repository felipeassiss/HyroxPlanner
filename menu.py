from utils import criar_arquivo, limpar, pausa
from config import ARQUIVO

from treinos import (
    adicionar_treino, 
    listar_treinos, 
    buscar_treino, 
    editar_treino, 
    excluir_treino,
    analisar_historico  # <-- Função de análise importada aqui
)

from competicoes import cadastrar_competicao, visualizar_competicoes
from agente_ia import falar_com_agente

def menu_principal():
    criar_arquivo()

    while True:
        limpar()

        print("======== HYROX PLANNER ========")
        print("1 - Cadastrar treino")
        print("2 - Listar treinos")
        print("3 - Buscar treino")
        print("4 - Editar treino")
        print("5 - Excluir treino")
        print("-" * 31)
        print("6 - Cadastrar competição")
        print("7 - Visualizar competições")
        print("-" * 31)
        print("8 - Assistente IA (Falar com Agente)")
        print("9 - Análise Inteligente do Histórico") # <-- Nova opção adicionada no menu visual
        print("0 - Sair")
        print("===============================")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_treino()
        elif opcao == "2":
            listar_treinos()
        elif opcao == "3":
            buscar_treino()
        elif opcao == "4":
            editar_treino()
        elif opcao == "5":
            excluir_treino()
        elif opcao == "6":
            cadastrar_competicao()
        elif opcao == "7":
            visualizar_competicoes()
        elif opcao == "8":
            limpar()
            print("=== ASSISTENTE INTELIGENTE ===\n")
            falar_com_agente(ARQUIVO, "Hyrox Planner")
            pausa()
        elif opcao == "9":
            analisar_historico()
        elif opcao == "0":
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOpção inválida.")
            pausa()