from menu import menu_principal
import csv
import os
from menu import (
    banner, menu_principal, tela_saida,
    titulo, subtitulo, caixa_mensagem,
    opcao_menu, input_estilizado, pressione_enter,
    linha, separador, cor, limpar_tela,
    cronometro, conversor_ritmo, contador_regressivo
)

# ╔══════════════════════════════════════════════════════════════╗
#                    CONFIGURAÇÕES DO ARQUIVO
# ╚══════════════════════════════════════════════════════════════╝

ARQUIVO = "dados.csv"
CAMPOS  = ["id", "nome", "email", "telefone"]


# ╔══════════════════════════════════════════════════════════════╗
#                    FUNÇÕES DE DADOS
# ╚══════════════════════════════════════════════════════════════╝

def inicializar_arquivo():
    """Cria o arquivo CSV com cabeçalho se não existir."""
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CAMPOS)
            writer.writeheader()


def ler_registros():
    """Retorna todos os registros do CSV como lista de dicionários."""
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def salvar_todos(registros):
    """Sobrescreve o arquivo com a lista de registros fornecida."""
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writeheader()
        writer.writerows(registros)


def proximo_id(registros):
    """Gera o próximo ID sequencial."""
    if not registros:
        return 1
    return max(int(r["id"]) for r in registros) + 1


# ╔══════════════════════════════════════════════════════════════╗
#                    OPERAÇÃO: SALVAR
# ╚══════════════════════════════════════════════════════════════╝

def salvar_registro():
    titulo("Novo Registro", "verde")
    subtitulo("Preencha os dados")

    nome     = input_estilizado("Nome completo")
    email    = input_estilizado("E-mail")
    telefone = input_estilizado("Telefone")

    if not nome.strip():
        caixa_mensagem("Nome não pode ser vazio!", "erro")
        pressione_enter()
        return

    registros = ler_registros()
    novo = {
        "id":       proximo_id(registros),
        "nome":     nome.strip(),
        "email":    email.strip(),
        "telefone": telefone.strip()
    }
    registros.append(novo)
    salvar_todos(registros)

    caixa_mensagem("Registro #" + str(novo["id"]) + " salvo com sucesso!", "sucesso")
    pressione_enter()


# ╔══════════════════════════════════════════════════════════════╗
#                    OPERAÇÃO: LISTAR
# ╚══════════════════════════════════════════════════════════════╝

def listar_registros():
    titulo("Todos os Registros", "ciano")
    registros = ler_registros()

    if not registros:
        caixa_mensagem("Nenhum registro encontrado.", "aviso")
        pressione_enter()
        return

    # Cabeçalho da tabela
    print(cor("  " + "ID".ljust(6) + "NOME".ljust(
        
        2) + "E-MAIL".ljust(28) + "TELEFONE", "amarelo"))
    linha(char="─", cor_linha="cinza")

    for r in registros:
        id_colorido    = cor(str(r["id"]).ljust(6), "ciano")
        nome_fmt       = r["nome"].ljust(22)
        email_colorido = cor(r["email"].ljust(28), "cinza")
        telefone_fmt   = r["telefone"]
        print("  " + id_colorido + nome_fmt + email_colorido + telefone_fmt)

    print()
    print(cor("  Total: " + str(len(registros)) + " registro(s)", "cinza"))
    pressione_enter()


# ╔══════════════════════════════════════════════════════════════╗
#                    OPERAÇÃO: ATUALIZAR
# ╚══════════════════════════════════════════════════════════════╝

def atualizar_registro():
    titulo("Atualizar Registro", "amarelo")
    registros = ler_registros()

    if not registros:
        caixa_mensagem("Nenhum registro para atualizar.", "aviso")
        pressione_enter()
        return

    id_busca = input_estilizado("Digite o ID do registro a atualizar")

    encontrado = None
    for r in registros:
        if r["id"] == id_busca.strip():
            encontrado = r
            break

    if not encontrado:
        caixa_mensagem("Registro #" + id_busca + " não encontrado!", "erro")
        pressione_enter()
        return

    subtitulo("Editando registro #" + encontrado["id"])
    print(cor("  Nome atual:     " + encontrado["nome"], "cinza"))
    print(cor("  E-mail atual:   " + encontrado["email"], "cinza"))
    print(cor("  Telefone atual: " + encontrado["telefone"], "cinza"))
    print()
    print(cor("  (Deixe em branco para manter o valor atual)", "cinza"))

    novo_nome     = input_estilizado("Novo nome")
    novo_email    = input_estilizado("Novo e-mail")
    novo_telefone = input_estilizado("Novo telefone")

    if novo_nome.strip():
        encontrado["nome"] = novo_nome.strip()
    if novo_email.strip():
        encontrado["email"] = novo_email.strip()
    if novo_telefone.strip():
        encontrado["telefone"] = novo_telefone.strip()

    salvar_todos(registros)
    caixa_mensagem("Registro #" + id_busca + " atualizado com sucesso!", "sucesso")
    pressione_enter()


# ╔══════════════════════════════════════════════════════════════╗
#                    OPERAÇÃO: APAGAR
# ╚══════════════════════════════════════════════════════════════╝

def apagar_registro():
    titulo("Apagar Registro", "vermelho")
    registros = ler_registros()

    if not registros:
        caixa_mensagem("Nenhum registro para apagar.", "aviso")
        pressione_enter()
        return

    id_busca = input_estilizado("Digite o ID do registro a apagar")

    encontrado = None
    for r in registros:
        if r["id"] == id_busca.strip():
            encontrado = r
            break

    if not encontrado:
        caixa_mensagem("Registro #" + id_busca + " não encontrado!", "erro")
        pressione_enter()
        return

    subtitulo("Confirmar exclusão")
    print(cor("  Nome:     " + encontrado["nome"], "branco"))
    print(cor("  E-mail:   " + encontrado["email"], "branco"))
    print(cor("  Telefone: " + encontrado["telefone"], "branco"))
    print()

    confirmacao = input_estilizado(cor("Tem certeza? Digite S para confirmar", "vermelho"))

    if confirmacao.strip().upper() == "S":
        novos = [r for r in registros if r["id"] != id_busca.strip()]
        salvar_todos(novos)
        caixa_mensagem("Registro #" + id_busca + " apagado com sucesso!", "sucesso")
    else:
        caixa_mensagem("Operação cancelada.", "aviso")

    pressione_enter()


# ╔══════════════════════════════════════════════════════════════╗
#                    LOOP PRINCIPAL
# ╚══════════════════════════════════════════════════════════════╝

def main():
    inicializar_arquivo()
    banner()

    acoes = {
        "1": salvar_registro,
        "2": listar_registros,
        "3": atualizar_registro,
        "4": apagar_registro,
        "5": cronometro,
        "6": conversor_ritmo,
        "7": contador_regressivo,
    }

    while True:
        escolha = menu_principal()

        if escolha == "0":
            tela_saida()
            break
        elif escolha in acoes:
            acoes[escolha]()
        else:
            caixa_mensagem("Opção inválida! Tente novamente.", "erro")
            pressione_enter()


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    menu_principal()
    
