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

import os
import time
import threading

# ╔══════════════════════════════════════════════════════════════╗
#                    CONFIGURAÇÕES VISUAIS
# ╚══════════════════════════════════════════════════════════════╝

CORES = {
    "reset":    "\033[0m",
    "negrito":  "\033[1m",
    "verde":    "\033[92m",
    "amarelo":  "\033[93m",
    "azul":     "\033[94m",
    "ciano":    "\033[96m",
    "vermelho": "\033[91m",
    "branco":   "\033[97m",
    "cinza":    "\033[90m",
    "roxo":     "\033[95m",
    "bg_azul":  "\033[44m",
    "bg_verde": "\033[42m",
}

LARGURA = 60


# ╔══════════════════════════════════════════════════════════════╗
#                    LIMPEZA DE TELA
# ╚══════════════════════════════════════════════════════════════╝

def limpar_tela():
    """Limpa o terminal independente do sistema operacional."""
    os.system("cls" if os.name == "nt" else "clear")


# ╔══════════════════════════════════════════════════════════════╗
#                    ORGANIZAÇÃO VISUAL
# ╚══════════════════════════════════════════════════════════════╝

def cor(texto, *estilos):
    """Aplica uma ou mais cores/estilos ao texto."""
    estilo = "".join(CORES.get(e, "") for e in estilos)
    return f"{estilo}{texto}{CORES['reset']}"


def linha(char="═", largura=LARGURA, cor_linha="ciano"):
    """Imprime uma linha decorativa."""
    print(cor(char * largura, cor_linha))


def linha_dupla(largura=LARGURA):
    print(cor("╔" + "═" * (largura - 2) + "╗", "ciano"))


def linha_dupla_baixo(largura=LARGURA):
    print(cor("╚" + "═" * (largura - 2) + "╝", "ciano"))


def titulo(texto, cor_texto="amarelo"):
    """Imprime um título centralizado com bordas decorativas."""
    limpar_tela()
    linha_dupla()
    texto_formatado = texto.upper().center(LARGURA - 2)
    print(cor("║", "ciano") + cor(texto_formatado, cor_texto, "negrito") + cor("║", "ciano"))
    linha_dupla_baixo()
    print()


def subtitulo(texto, cor_texto="ciano"):
    """Imprime um subtítulo com linha abaixo."""
    print()
    print(cor(f"  ◈ {texto}", cor_texto, "negrito"))
    print(cor("  " + "─" * (LARGURA - 4), "cinza"))


def caixa_mensagem(texto, tipo="info"):
    """Imprime uma mensagem em caixa colorida."""
    icones = {
        "info":    ("ℹ", "azul"),
        "sucesso": ("✔", "verde"),
        "erro":    ("✘", "vermelho"),
        "aviso":   ("⚠", "amarelo"),
    }
    icone, cor_tipo = icones.get(tipo, ("•", "branco"))
    print()
    print(cor(f"  ┌{'─' * (LARGURA - 4)}┐", cor_tipo))
    print(cor(f"  │ {icone} {texto:<{LARGURA - 6}}│", cor_tipo))
    print(cor(f"  └{'─' * (LARGURA - 4)}┘", cor_tipo))
    print()


def opcao_menu(numero, texto, cor_num="amarelo", cor_txt="branco"):
    """Imprime uma opção de menu formatada."""
    print(f"  {cor(f'[{numero}]', cor_num, 'negrito')}  {cor(texto, cor_txt)}")


def pressione_enter():
    """Pausa a execução até o usuário pressionar Enter."""
    print()
    input(cor("  Pressione ENTER para continuar...", "cinza"))


def input_estilizado(pergunta, cor_pergunta="ciano"):
    """Input com estilo visual."""
    return input(cor(f"\n  ▶ {pergunta}: ", cor_pergunta, "negrito"))


def separador():
    """Imprime um separador simples."""
    print(cor("  " + "· " * (LARGURA // 2 - 1), "cinza"))


# ╔══════════════════════════════════════════════════════════════╗
#                    BANNER INICIAL
# ╚══════════════════════════════════════════════════════════════╝

def banner():
    """Exibe o banner principal do sistema."""
    limpar_tela()
    print()
    print(cor("  ╔══════════════════════════════════════════════════════╗", "ciano"))
    print(cor("  ║", "ciano") + cor("                                                      ", "bg_azul") + cor("║", "ciano"))
    print(cor("  ║", "ciano") + cor("        📁  SISTEMA DE GESTÃO DE DADOS  📁            ", "bg_azul") + cor("║", "ciano"))
    print(cor("  ║", "ciano") + cor("                                                      ", "bg_azul") + cor("║", "ciano"))
    print(cor("  ║", "ciano") + cor("         Fundamentos da Programação — 2026            ", "azul") + cor("║", "ciano"))
    print(cor("  ╚══════════════════════════════════════════════════════╝", "ciano"))
    print()
    time.sleep(0.8)


# ╔══════════════════════════════════════════════════════════════╗
#                    MENU PRINCIPAL
# ╚══════════════════════════════════════════════════════════════╝

def menu_principal():
    """Exibe e retorna a opção do menu principal."""
    titulo("Sistema de Gestão de Dados")

    subtitulo("DADOS")
    opcao_menu("1", "Salvar novo registro")
    opcao_menu("2", "Listar todos os registros")
    opcao_menu("3", "Atualizar um registro")
    opcao_menu("4", "Apagar um registro")

    subtitulo("FERRAMENTAS")
    opcao_menu("5", "Cronômetro")
    opcao_menu("6", "Conversor de ritmo (Pace)")
    opcao_menu("7", "Contador regressivo")

    subtitulo("SISTEMA")
    opcao_menu("0", "Sair", cor_num="vermelho", cor_txt="cinza")

    print()
    linha(char="─", cor_linha="cinza")
    escolha = input_estilizado("Escolha uma opção", "amarelo")
    return escolha.strip()


# ╔══════════════════════════════════════════════════════════════╗
#              FUNCIONALIDADE EXTRA 1 — CRONÔMETRO
# ╚══════════════════════════════════════════════════════════════╝

def cronometro():
    """Cronômetro interativo com start/stop."""
    titulo("Cronômetro", "verde")
    caixa_mensagem("ENTER para iniciar  •  ENTER para parar", "info")

    input(cor("  Pressione ENTER para INICIAR...", "verde"))
    inicio = time.time()

    rodando = [True]

    def mostrar_tempo():
        while rodando[0]:
            decorrido = time.time() - inicio
            horas   = int(decorrido // 3600)
            minutos = int((decorrido % 3600) // 60)
            segundos = decorrido % 60
            display = f"  ⏱  {horas:02d}:{minutos:02d}:{segundos:05.2f}"
            print(cor(display, "amarelo", "negrito"), end="\r")
            time.sleep(0.05)

    thread = threading.Thread(target=mostrar_tempo, daemon=True)
    thread.start()

    input()  # Aguarda o segundo ENTER
    rodando[0] = False
    time.sleep(0.1)

    decorrido = time.time() - inicio
    horas   = int(decorrido // 3600)
    minutos = int((decorrido % 3600) // 60)
    segundos = decorrido % 60

    print()
    caixa_mensagem(f"Tempo final: {horas:02d}:{minutos:02d}:{segundos:05.2f}", "sucesso")
    pressione_enter()


# ╔══════════════════════════════════════════════════════════════╗
#          FUNCIONALIDADE EXTRA 2 — CONVERSOR DE RITMO
# ╚══════════════════════════════════════════════════════════════╝

def conversor_ritmo():
    """Converte entre pace (min/km) e velocidade (km/h)."""
    titulo("Conversor de Ritmo", "roxo")

    subtitulo("ESCOLHA A CONVERSÃO")
    opcao_menu("1", "Pace (min/km)  →  Velocidade (km/h)")
    opcao_menu("2", "Velocidade (km/h)  →  Pace (min/km)")
    opcao_menu("0", "Voltar", "vermelho", "cinza")

    escolha = input_estilizado("Opção")

    if escolha == "1":
        subtitulo("PACE → VELOCIDADE")
        try:
            minutos = float(input_estilizado("Minutos do pace (ex: 5)"))
            segundos = float(input_estilizado("Segundos do pace (ex: 30)"))
            pace_total = minutos + segundos / 60
            if pace_total <= 0:
                raise ValueError
            velocidade = 60 / pace_total
            caixa_mensagem(
                f"Pace {int(minutos):02d}:{int(segundos):02d} min/km  =  {velocidade:.2f} km/h",
                "sucesso"
            )
        except ValueError:
            caixa_mensagem("Valor inválido!", "erro")

    elif escolha == "2":
        subtitulo("VELOCIDADE → PACE")
        try:
            velocidade = float(input_estilizado("Velocidade em km/h (ex: 10.5)"))
            if velocidade <= 0:
                raise ValueError
            pace_total = 60 / velocidade
            minutos = int(pace_total)
            segundos = int((pace_total - minutos) * 60)
            caixa_mensagem(
                f"{velocidade:.2f} km/h  =  Pace {minutos:02d}:{segundos:02d} min/km",
                "sucesso"
            )
        except ValueError:
            caixa_mensagem("Valor inválido!", "erro")

    pressione_enter()


# ╔══════════════════════════════════════════════════════════════╗
#         FUNCIONALIDADE EXTRA 3 — CONTADOR REGRESSIVO
# ╚══════════════════════════════════════════════════════════════╝

def contador_regressivo():
    """Contador regressivo com animação visual."""
    titulo("Contador Regressivo", "vermelho")

    try:
        minutos = int(input_estilizado("Minutos (0 se não quiser)"))
        segundos = int(input_estilizado("Segundos"))
        total = minutos * 60 + segundos

        if total <= 0:
            caixa_mensagem("Tempo deve ser maior que zero!", "erro")
            pressione_enter()
            return

        print()
        while total > 0:
            mins = total // 60
            segs = total % 60
            barra_tamanho = 30
            progresso = int((total / (minutos * 60 + segundos)) * barra_tamanho)
            barra = "█" * progresso + "░" * (barra_tamanho - progresso)

            display = (
                f"  {cor(f'⏳ {mins:02d}:{segs:02d}', 'amarelo', 'negrito')}  "
                f"{cor(barra, 'verde')}  "
                f"{cor(str(total) + 's', 'cinza')}"
            )
            print(display, end="\r")
            time.sleep(1)
            total -= 1

        print()
        print()
        caixa_mensagem("⏰  Tempo esgotado!", "sucesso")
        # Bip sonoro (funciona em alguns terminais)
        print("\a", end="")

    except ValueError:
        caixa_mensagem("Digite apenas números inteiros!", "erro")

    pressione_enter()


# ╔══════════════════════════════════════════════════════════════╗
#                    TELA DE SAÍDA
# ╚══════════════════════════════════════════════════════════════╝

def tela_saida():
    """Exibe mensagem de encerramento."""
    limpar_tela()
    print()
    linha()
    print(cor("  Obrigado por usar o Sistema de Gestão de Dados!".center(LARGURA), "verde", "negrito"))
    print(cor("  Fundamentos da Programação — 2025".center(LARGURA), "cinza"))
    linha()
    print()
import os
import time
import threading

# ╔══════════════════════════════════════════════════════════════╗
#                    CONFIGURAÇÕES VISUAIS
# ╚══════════════════════════════════════════════════════════════╝

CORES = {
    "reset":    "\033[0m",
    "negrito":  "\033[1m",
    "verde":    "\033[92m",
    "amarelo":  "\033[93m",
    "azul":     "\033[94m",
    "ciano":    "\033[96m",
    "vermelho": "\033[91m",
    "branco":   "\033[97m",
    "cinza":    "\033[90m",
    "roxo":     "\033[95m",
    "bg_azul":  "\033[44m",
    "bg_verde": "\033[42m",
}

LARGURA = 60


# ╔══════════════════════════════════════════════════════════════╗
#                    LIMPEZA DE TELA
# ╚══════════════════════════════════════════════════════════════╝

def limpar_tela():
    """Limpa o terminal independente do sistema operacional."""
    os.system("cls" if os.name == "nt" else "clear")


# ╔══════════════════════════════════════════════════════════════╗
#                    ORGANIZAÇÃO VISUAL
# ╚══════════════════════════════════════════════════════════════╝

def cor(texto, *estilos):
    """Aplica uma ou mais cores/estilos ao texto."""
    estilo = "".join(CORES.get(e, "") for e in estilos)
    return f"{estilo}{texto}{CORES['reset']}"


def linha(char="═", largura=LARGURA, cor_linha="ciano"):
    """Imprime uma linha decorativa."""
    print(cor(char * largura, cor_linha))


def linha_dupla(largura=LARGURA):
    print(cor("╔" + "═" * (largura - 2) + "╗", "ciano"))


def linha_dupla_baixo(largura=LARGURA):
    print(cor("╚" + "═" * (largura - 2) + "╝", "ciano"))


def titulo(texto, cor_texto="amarelo"):
    """Imprime um título centralizado com bordas decorativas."""
    limpar_tela()
    linha_dupla()
    texto_formatado = texto.upper().center(LARGURA - 2)
    print(cor("║", "ciano") + cor(texto_formatado, cor_texto, "negrito") + cor("║", "ciano"))
    linha_dupla_baixo()
    print()


def subtitulo(texto, cor_texto="ciano"):
    """Imprime um subtítulo com linha abaixo."""
    print()
    print(cor(f"  ◈ {texto}", cor_texto, "negrito"))
    print(cor("  " + "─" * (LARGURA - 4), "cinza"))


def caixa_mensagem(texto, tipo="info"):
    """Imprime uma mensagem em caixa colorida."""
    icones = {
        "info":    ("ℹ", "azul"),
        "sucesso": ("✔", "verde"),
        "erro":    ("✘", "vermelho"),
        "aviso":   ("⚠", "amarelo"),
    }
    icone, cor_tipo = icones.get(tipo, ("•", "branco"))
    print()
    print(cor(f"  ┌{'─' * (LARGURA - 4)}┐", cor_tipo))
    print(cor(f"  │ {icone} {texto:<{LARGURA - 6}}│", cor_tipo))
    print(cor(f"  └{'─' * (LARGURA - 4)}┘", cor_tipo))
    print()


def opcao_menu(numero, texto, cor_num="amarelo", cor_txt="branco"):
    """Imprime uma opção de menu formatada."""
    print(f"  {cor(f'[{numero}]', cor_num, 'negrito')}  {cor(texto, cor_txt)}")


def pressione_enter():
    """Pausa a execução até o usuário pressionar Enter."""
    print()
    input(cor("  Pressione ENTER para continuar...", "cinza"))


def input_estilizado(pergunta, cor_pergunta="ciano"):
    """Input com estilo visual."""
    return input(cor(f"\n  ▶ {pergunta}: ", cor_pergunta, "negrito"))


def separador():
    """Imprime um separador simples."""
    print(cor("  " + "· " * (LARGURA // 2 - 1), "cinza"))


# ╔══════════════════════════════════════════════════════════════╗
#                    BANNER INICIAL
# ╚══════════════════════════════════════════════════════════════╝

def banner():
    """Exibe o banner principal do sistema."""
    limpar_tela()
    print()
    print(cor("  ╔══════════════════════════════════════════════════════╗", "ciano"))
    print(cor("  ║", "ciano") + cor("                                                      ", "bg_azul") + cor("║", "ciano"))
    print(cor("  ║", "ciano") + cor("        📁  SISTEMA DE GESTÃO DE DADOS  📁            ", "bg_azul") + cor("║", "ciano"))
    print(cor("  ║", "ciano") + cor("                                                      ", "bg_azul") + cor("║", "ciano"))
    print(cor("  ║", "ciano") + cor("         Fundamentos da Programação — 2025            ", "azul") + cor("║", "ciano"))
    print(cor("  ╚══════════════════════════════════════════════════════╝", "ciano"))
    print()
    time.sleep(0.8)


# ╔══════════════════════════════════════════════════════════════╗
#                    MENU PRINCIPAL
# ╚══════════════════════════════════════════════════════════════╝

def menu_principal():
    """Exibe e retorna a opção do menu principal."""
    titulo("Sistema de Gestão de Dados")

    subtitulo("DADOS")
    opcao_menu("1", "Salvar novo registro")
    opcao_menu("2", "Listar todos os registros")
    opcao_menu("3", "Atualizar um registro")
    opcao_menu("4", "Apagar um registro")

    subtitulo("FERRAMENTAS")
    opcao_menu("5", "Cronômetro")
    opcao_menu("6", "Conversor de ritmo (Pace)")
    opcao_menu("7", "Contador regressivo")

    subtitulo("SISTEMA")
    opcao_menu("0", "Sair", cor_num="vermelho", cor_txt="cinza")

    print()
    linha(char="─", cor_linha="cinza")
    escolha = input_estilizado("Escolha uma opção", "amarelo")
    return escolha.strip()


# ╔══════════════════════════════════════════════════════════════╗
#              FUNCIONALIDADE EXTRA 1 — CRONÔMETRO
# ╚══════════════════════════════════════════════════════════════╝

def cronometro():
    """Cronômetro interativo com start/stop."""
    titulo("Cronômetro", "verde")
    caixa_mensagem("ENTER para iniciar  •  ENTER para parar", "info")

    input(cor("  Pressione ENTER para INICIAR...", "verde"))
    inicio = time.time()

    rodando = [True]

    def mostrar_tempo():
        while rodando[0]:
            decorrido = time.time() - inicio
            horas   = int(decorrido // 3600)
            minutos = int((decorrido % 3600) // 60)
            segundos = decorrido % 60
            display = f"  ⏱  {horas:02d}:{minutos:02d}:{segundos:05.2f}"
            print(cor(display, "amarelo", "negrito"), end="\r")
            time.sleep(0.05)

    thread = threading.Thread(target=mostrar_tempo, daemon=True)
    thread.start()

    input()  # Aguarda o segundo ENTER
    rodando[0] = False
    time.sleep(0.1)

    decorrido = time.time() - inicio
    horas   = int(decorrido // 3600)
    minutos = int((decorrido % 3600) // 60)
    segundos = decorrido % 60

    print()
    caixa_mensagem(f"Tempo final: {horas:02d}:{minutos:02d}:{segundos:05.2f}", "sucesso")
    pressione_enter()


# ╔══════════════════════════════════════════════════════════════╗
#          FUNCIONALIDADE EXTRA 2 — CONVERSOR DE RITMO
# ╚══════════════════════════════════════════════════════════════╝

def conversor_ritmo():
    """Converte entre pace (min/km) e velocidade (km/h)."""
    titulo("Conversor de Ritmo", "roxo")

    subtitulo("ESCOLHA A CONVERSÃO")
    opcao_menu("1", "Pace (min/km)  →  Velocidade (km/h)")
    opcao_menu("2", "Velocidade (km/h)  →  Pace (min/km)")
    opcao_menu("0", "Voltar", "vermelho", "cinza")

    escolha = input_estilizado("Opção")

    if escolha == "1":
        subtitulo("PACE → VELOCIDADE")
        try:
            minutos = float(input_estilizado("Minutos do pace (ex: 5)"))
            segundos = float(input_estilizado("Segundos do pace (ex: 30)"))
            pace_total = minutos + segundos / 60
            if pace_total <= 0:
                raise ValueError
            velocidade = 60 / pace_total
            caixa_mensagem(
                f"Pace {int(minutos):02d}:{int(segundos):02d} min/km  =  {velocidade:.2f} km/h",
                "sucesso"
            )
        except ValueError:
            caixa_mensagem("Valor inválido!", "erro")

    elif escolha == "2":
        subtitulo("VELOCIDADE → PACE")
        try:
            velocidade = float(input_estilizado("Velocidade em km/h (ex: 10.5)"))
            if velocidade <= 0:
                raise ValueError
            pace_total = 60 / velocidade
            minutos = int(pace_total)
            segundos = int((pace_total - minutos) * 60)
            caixa_mensagem(
                f"{velocidade:.2f} km/h  =  Pace {minutos:02d}:{segundos:02d} min/km",
                "sucesso"
            )
        except ValueError:
            caixa_mensagem("Valor inválido!", "erro")

    pressione_enter()


# ╔══════════════════════════════════════════════════════════════╗
#         FUNCIONALIDADE EXTRA 3 — CONTADOR REGRESSIVO
# ╚══════════════════════════════════════════════════════════════╝

def contador_regressivo():
    """Contador regressivo com animação visual."""
    titulo("Contador Regressivo", "vermelho")

    try:
        minutos = int(input_estilizado("Minutos (0 se não quiser)"))
        segundos = int(input_estilizado("Segundos"))
        total = minutos * 60 + segundos

        if total <= 0:
            caixa_mensagem("Tempo deve ser maior que zero!", "erro")
            pressione_enter()
            return

        print()
        while total > 0:
            mins = total // 60
            segs = total % 60
            barra_tamanho = 30
            progresso = int((total / (minutos * 60 + segundos)) * barra_tamanho)
            barra = "█" * progresso + "░" * (barra_tamanho - progresso)

            display = (
                f"  {cor(f'⏳ {mins:02d}:{segs:02d}', 'amarelo', 'negrito')}  "
                f"{cor(barra, 'verde')}  "
                f"{cor(str(total) + 's', 'cinza')}"
            )
            print(display, end="\r")
            time.sleep(1)
            total -= 1

        print()
        print()
        caixa_mensagem("⏰  Tempo esgotado!", "sucesso")
        # Bip sonoro (funciona em alguns terminais)
        print("\a", end="")

    except ValueError:
        caixa_mensagem("Digite apenas números inteiros!", "erro")

    pressione_enter()


# ╔══════════════════════════════════════════════════════════════╗
#                    TELA DE SAÍDA
# ╚══════════════════════════════════════════════════════════════╝

def tela_saida():
    """Exibe mensagem de encerramento."""
    limpar_tela()
    print()
    linha()
    print(cor("  Obrigado por usar o Sistema de Gestão de Dados!".center(LARGURA), "verde", "negrito"))
    print(cor("  Fundamentos da Programação — 2026 ".center(LARGURA), "cinza"))
    linha()
    print()



