import os
import csv
from config import ARQUIVO

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def pausa():
    input("\nENTER para continuar...")

def validar_texto(texto):
    while texto.strip() == "":
        texto = input("Campo vazio. Digite novamente: ")
    return texto

def criar_arquivo():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([
                "ID", "Nome", "Tipo", "Data", "Duracao", "Intensidade"
            ])

def gerar_id():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            linhas = list(csv.reader(arquivo))

            if len(linhas) <= 1:
                return 1

            ultimo_id = int(linhas[-1][0])
            return ultimo_id + 1
    except:
        return 1