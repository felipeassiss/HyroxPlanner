import os
import time
import threading
#adiciona menu
# ╔══════════════════════════════════════════════════════════════╗
#                    IMPORTAÇÕES DO REPOSITÓRIO
# ╚══════════════════════════════════════════════════════════════╝
from utils import criar_arquivo
from config import ARQUIVO

from treinos import (
    adicionar_treino,
    listar_treinos,
    buscar_treino,
    editar_treino,
    excluir_treino,
    analisar_historico,
    cadastrar_exercicio,
    listar_exercicios,
    evolucao_atleta,
    _criar_arquivo_func,
)

from competicoes import cadastrar_competicao, visualizar_competicoes
from agente_ia import falar_com_agente

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
    """Pausa a execução até o utilizador pressionar Enter."""
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
    print(cor("  ║", "ciano") + cor("         🏋️‍♂️  SISTEMA HYROX PLANNER  🏋️‍♂️                ", "bg_azul") + cor("║", "ciano"))
    print(cor("  ║", "ciano") + cor("                                                      ", "bg_azul") + cor("║", "ciano"))
    print(cor("  ║", "ciano") + cor("         Fundamentos da Programação — 2026            ", "azul") + cor("║", "ciano"))
    print(cor("  ╚══════════════════════════════════════════════════════╝", "ciano"))
    print()
    time.sleep(0.8)

# ╔══════════════════════════════════════════════════════════════╗
#                    MENU PRINCIPAL
# ╚══════════════════════════════════════════════════════════════╝

def menu_principal():
    """Exibe e gerencia as opções principais mescladas com o repositório."""
    criar_arquivo()
    _criar_arquivo_func()

    while True:
        titulo("Hyrox Planner")

        subtitulo("TREINOS")
        opcao_menu("1", "Cadastrar treino")
        opcao_menu("2", "Listar treinos")
        opcao_menu("3", "Buscar treino")
        opcao_menu("4", "Editar treino")
        opcao_menu("5", "Excluir treino")

        subtitulo("EXERCÍCIOS HYROX")
        opcao_menu("6",  "Cadastrar exercício")
        opcao_menu("7",  "Listar exercícios")
        opcao_menu("8",  "Evolução do atleta")

        subtitulo("COMPETIÇÕES")
        opcao_menu("9",  "Cadastrar competição")
        opcao_menu("10", "Visualizar competições")

        subtitulo("INTELIGÊNCIA ARTIFICIAL")
        opcao_menu("11", "Assistente IA (Falar com Agente)", cor_num="roxo", cor_txt="roxo")
        opcao_menu("12", "Análise Inteligente do Histórico")

        subtitulo("FERRAMENTAS EXTRAS")
        opcao_menu("13", "Cronômetro")
        opcao_menu("14", "Conversor de ritmo (Pace)")
        opcao_menu("15", "Contador regressivo")

        subtitulo("SISTEMA")
        opcao_menu("0", "Sair", cor_num="vermelho", cor_txt="cinza")

        print()
        linha(char="─", cor_linha="cinza")
        escolha = input_estilizado("Escolha uma opção", "amarelo").strip()

        if escolha == "1":
            adicionar_treino()
        elif escolha == "2":
            listar_treinos()
        elif escolha == "3":
            buscar_treino()
        elif escolha == "4":
            editar_treino()
        elif escolha == "5":
            excluir_treino()
        elif escolha == "6":
            cadastrar_exercicio()
        elif escolha == "7":
            listar_exercicios()
        elif escolha == "8":
            evolucao_atleta()
        elif escolha == "9":
            cadastrar_competicao()
        elif escolha == "10":
            visualizar_competicoes()
        elif escolha == "11":
            limpar_tela()
            print(cor("\n=== ASSISTENTE INTELIGENTE ===\n", "roxo", "negrito"))
            falar_com_agente(ARQUIVO, "Hyrox Planner")
            pressione_enter()
        elif escolha == "12":
            analisar_historico()
        elif escolha == "13":
            cronometro()
        elif escolha == "14":
            conversor_ritmo()
        elif escolha == "15":
            contador_regressivo()
        elif escolha == "0":
            tela_saida()
            break
        else:
            caixa_mensagem("Opção inválida.", "erro")
            pressione_enter()

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
    print(cor("  Obrigado por usar o Hyrox Planner!  ".center(LARGURA), "verde", "negrito"))
    print(cor("  Fundamentos da Programação — 2026 ".center(LARGURA), "cinza"))
    linha()
    print()

# Ponto de entrada se executado diretamente
if __name__ == "__main__":
    banner()
    menu_principal()
