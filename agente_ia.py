"""
agente.py — Módulo do Agente LLM (usando biblioteca oficial groq)
CESAR School | Disciplina 00004 | 2026.1

Implementa RAG simplificado usando a biblioteca oficial da Groq.
"""

from groq import Groq
from dotenv import load_dotenv
import os


# ============================================================================
# CONFIGURAÇÃO DA API
# ============================================================================

# ⚠️ INSTRUÇÕES PARA OBTER A CHAVE:
# 
# 1. Acesse: https://console.groq.com
# 2. Crie uma conta (gratuita)
# 3. Vá em "API Keys" no menu lateral
# 4. Clique em "Create API Key"
# 5. Copie a chave que começa com "gsk_..."
# 6. Cole abaixo OU configure como variável de ambiente GROQ_API_KEY

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Configuração
GROQ_MODEL = "llama-3.3-70b-versatile"


# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def falar_com_agente(nome_arquivo: str, nome_sistema: str = "Sistema") -> str:
    """
    Lê um arquivo .csv ou .txt e permite ao usuário fazer perguntas
    sobre os dados usando um LLM via biblioteca Groq.
    
    Args:
        nome_arquivo: caminho para o arquivo de dados do projeto
        nome_sistema: nome do sistema exibido no prompt do LLM
    
    Returns:
        A resposta do LLM como string
    """
    
    # ------------------------------------------------------------------------
    # 1. LEITURA DO ARQUIVO
    # ------------------------------------------------------------------------
    
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
    
    except FileNotFoundError:
        msg = f"\n[Agente] ❌ Arquivo '{nome_arquivo}' não encontrado."
        msg += "\n         Verifique se o caminho está correto."
        print(msg)
        return msg
    
    except PermissionError:
        msg = f"\n[Agente] ❌ Sem permissão para ler '{nome_arquivo}'."
        print(msg)
        return msg
    
    except Exception as erro:
        msg = f"\n[Agente] ❌ Erro ao ler o arquivo: {erro}"
        print(msg)
        return msg
    
    # Verificar se o arquivo está vazio
    if not conteudo.strip():
        msg = "\n[Agente] 📭 O arquivo está vazio."
        msg += "\n         Crie alguns registros antes de perguntar ao agente."
        print(msg)
        return msg
    
    # ------------------------------------------------------------------------
    # 2. OBTER PERGUNTA DO USUÁRIO
    # ------------------------------------------------------------------------
    
    print()
    pergunta = input("🤖 O que você quer perguntar sobre seus dados? > ").strip()
    
    if not pergunta:
        msg = "\n[Agente] ⚠️  Nenhuma pergunta digitada."
        print(msg)
        return msg
    
    # ------------------------------------------------------------------------
    # 3. MONTAGEM DO PROMPT
    # ------------------------------------------------------------------------
    
    prompt = f"""Você é um assistente inteligente do sistema {nome_sistema}.

Seu papel é analisar os dados fornecidos e responder perguntas do usuário de forma clara, objetiva e útil.

DADOS DO SISTEMA (formato CSV):
---
{conteudo}
---

PERGUNTA DO USUÁRIO: {pergunta}

INSTRUÇÕES PARA SUA RESPOSTA:
1. Responda SEMPRE em português do Brasil
2. Base sua resposta APENAS nos dados fornecidos acima
3. Se os dados não contêm informação suficiente, diga isso claramente
4. Seja objetivo e direto — evite repetir a pergunta ou fazer preâmbulos longos
5. Use formatação clara (listas, números) quando apropriado
6. Se identificar padrões ou insights interessantes nos dados, mencione-os

Responda agora:"""
    
    # ------------------------------------------------------------------------
    # 4. INICIALIZAR CLIENTE GROQ
    # ------------------------------------------------------------------------
    
    try:
        # Tentar usar variável de ambiente primeiro, depois a chave no código
        if GROQ_API_KEY and GROQ_API_KEY != "cole-sua-chave-aqui":
            client = Groq(api_key=GROQ_API_KEY)
        else:
            # Tenta usar variável de ambiente GROQ_API_KEY
            client = Groq()
    
    except Exception as erro:
        msg = "\n[Agente] ❌ Erro ao inicializar cliente Groq."
        msg += f"\n         {erro}"
        msg += "\n\n💡 CONFIGURE A CHAVE:"
        msg += "\n   Opção 1: Edite agente.py e cole a chave em GROQ_API_KEY"
        msg += "\n   Opção 2: Configure variável de ambiente: export GROQ_API_KEY=sua-chave"
        msg += "\n\n   Obtenha sua chave em: https://console.groq.com/keys"
        print(msg)
        return msg
    
    # ------------------------------------------------------------------------
    # 5. CHAMADA À API
    # ------------------------------------------------------------------------
    
    try:
        print("\n⏳ Consultando o agente...")
        
        # Criar completion (sem streaming para simplificar)
        completion = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_completion_tokens=1024,
            top_p=0.9,
            stream=False  # Desabilitado para ter resposta completa de uma vez
        )
        
        # Extrair resposta
        resposta = completion.choices[0].message.content
        
        # Exibir resposta formatada
        print("\n" + "=" * 70)
        print("🤖 AGENTE:")
        print("=" * 70)
        print(resposta)
        print("=" * 70)
        
        return resposta
    
    except Exception as erro:
        erro_str = str(erro)
        
        # Tratar erros comuns
        if "api_key" in erro_str.lower() or "authentication" in erro_str.lower():
            msg = "\n[Agente] ❌ Erro de autenticação."
            msg += "\n         Sua chave de API está inválida ou não foi configurada."
            msg += "\n\n💡 SOLUÇÃO:"
            msg += "\n   1. Acesse: https://console.groq.com/keys"
            msg += "\n   2. Gere uma nova chave de API"
            msg += "\n   3. Cole a chave em agente.py na linha: GROQ_API_KEY = '...'"
            msg += "\n   4. OU configure: export GROQ_API_KEY=sua-chave"
        
        elif "rate_limit" in erro_str.lower() or "429" in erro_str:
            msg = "\n[Agente] ⏸️  Limite de requisições excedido."
            msg += "\n         Aguarde alguns minutos e tente novamente."
            msg += "\n         (O plano gratuito da Groq tem limites de taxa)"
        
        elif "quota" in erro_str.lower() or "exceeded" in erro_str.lower():
            msg = "\n[Agente] 💳 Limite de uso excedido."
            msg += "\n         Sua conta gratuita atingiu o limite mensal."
            msg += "\n         Aguarde a renovação ou faça upgrade em console.groq.com"
        
        else:
            msg = f"\n[Agente] ❌ Erro ao consultar a API Groq:"
            msg += f"\n         {erro}"
        
        print(msg)
        return msg


# ============================================================================
# VERSÃO COM STREAMING (opcional)
# ============================================================================

def falar_com_agente_streaming(nome_arquivo: str, nome_sistema: str = "Sistema") -> str:
    """
    Versão alternativa que exibe a resposta em tempo real (streaming).
    
    Use esta função se quiser ver a resposta sendo gerada palavra por palavra,
    como no ChatGPT.
    """
    
    # Código de leitura e validação (igual à função principal)
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
    except FileNotFoundError:
        msg = f"\n[Agente] ❌ Arquivo '{nome_arquivo}' não encontrado."
        print(msg)
        return msg
    except Exception as erro:
        msg = f"\n[Agente] ❌ Erro ao ler arquivo: {erro}"
        print(msg)
        return msg
    
    if not conteudo.strip():
        msg = "\n[Agente] 📭 Arquivo vazio."
        print(msg)
        return msg
    
    print()
    pergunta = input("🤖 O que você quer perguntar sobre seus dados? > ").strip()
    
    if not pergunta:
        msg = "\n[Agente] ⚠️  Nenhuma pergunta digitada."
        print(msg)
        return msg
    
    prompt = f"""Você é um assistente do sistema {nome_sistema}.
Analise os dados CSV e responda em português do Brasil.

DADOS:
---
{conteudo}
---

PERGUNTA: {pergunta}

Responda de forma clara e objetiva baseando-se apenas nos dados acima."""
    
    try:
        if GROQ_API_KEY and GROQ_API_KEY != "cole-sua-chave-aqui":
            client = Groq(api_key=GROQ_API_KEY)
        else:
            client = Groq()
    except Exception as erro:
        msg = f"\n[Agente] ❌ Erro ao inicializar: {erro}"
        print(msg)
        return msg
    
    try:
        print("\n⏳ Consultando o agente...")
        print("\n" + "=" * 70)
        print("🤖 AGENTE (streaming):")
        print("=" * 70)
        
        # Criar completion com streaming
        completion = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_completion_tokens=1024,
            top_p=0.9,
            stream=True  # Habilitar streaming
        )
        
        # Coletar e exibir resposta em tempo real
        resposta_completa = ""
        for chunk in completion:
            conteudo_chunk = chunk.choices[0].delta.content or ""
            print(conteudo_chunk, end="", flush=True)
            resposta_completa += conteudo_chunk
        
        print("\n" + "=" * 70)
        
        return resposta_completa
    
    except Exception as erro:
        msg = f"\n[Agente] ❌ Erro: {erro}"
        print(msg)
        return msg


# ============================================================================
# TESTE DIRETO DO MÓDULO
# ============================================================================

if __name__ == "__main__":
    """
    Este bloco executa apenas quando agente.py é rodado diretamente.
    """
    
    print("=" * 70)
    print(" TESTE DO AGENTE LLM (Biblioteca Groq Oficial)")
    print("=" * 70)
    print()
    
    # Verificar configuração
    if not GROQ_API_KEY or GROQ_API_KEY == "cole-sua-chave-aqui":
        print("⚠️  Chave da API não configurada.")
        print()
        print("📋 Para configurar:")
        print("   1. Obtenha sua chave em: https://console.groq.com/keys")
        print("   2. Edite agente.py e cole a chave em GROQ_API_KEY")
        print("   3. OU configure: export GROQ_API_KEY=sua-chave")
        print()
    else:
        print(f"✅ Chave detectada: {GROQ_API_KEY[:15]}... ({len(GROQ_API_KEY)} chars)\n")
        
        # Criar arquivo de teste
        arquivo_teste = "teste_agente.csv"
        
        with open(arquivo_teste, "w", encoding="utf-8") as f:
            f.write("id,nome,categoria,valor,data_criacao\n")
            f.write("1,Notebook,Eletrônicos,3500.00,2026-05-20 10:30:00\n")
            f.write("2,Mouse,Eletrônicos,50.00,2026-05-21 14:15:00\n")
            f.write("3,Cadeira,Móveis,800.00,2026-05-22 09:00:00\n")
        
        print(f"✅ Arquivo de teste criado: {arquivo_teste}")
        print()
        
        # Testar o agente (versão normal)
        print("🧪 Testando versão normal (resposta completa):\n")
        falar_com_agente(arquivo_teste, "Sistema de Teste")
        
        # Opção: testar versão streaming
        # print("\n\n🧪 Testando versão streaming (tempo real):\n")
        # falar_com_agente_streaming(arquivo_teste, "Sistema de Teste")
        
        print()
        print("=" * 70)
        print("Teste concluído.")
        print("=" * 70)