# HyroxPlanner 🏋️‍♂️📊 (W.I.P) 🚧🛠️

O **HyroxPlanner** é um sistema de linha de comando (CLI) desenvolvido em Python para auxiliar no cadastro, visualização e organização de treinos HYROX, competições e simulações. 

## 🚀 Funcionalidades

**Domínio de Treinos (CRUD)**
- Cadastrar novos treinos (Nome, Tipo, Data, Duração e Intensidade)
- Listar todos os treinos registrados
- Buscar treinos específicos pelo nome
- Editar dados de um treino existente
- Excluir treinos do registro

**Domínio de Competições**
- Cadastrar novas competições (Nome, Data e Local)
- Visualizar competições com **contagem regressiva automática** de dias até o evento

**Assistente Inteligente (IA)**
- Integração com a API da Groq (LLM Llama 3) para ler, analisar e responder perguntas contextuais sobre o seu histórico de treinos.

## 💻 Tecnologias e Bibliotecas utilizadas

- **Python 3**
- Bibliotecas nativas: `csv`, `os`, `datetime`
- Bibliotecas externas: `groq` (Para a Inteligência Artificial), `python-dotenv` (Para segurança de senhas e variáveis de ambiente)

## 📁 Estrutura do Projeto

O código está organizado por **domínios de negócio**, facilitando a manutenção e escalabilidade:

- `treinos.py`: Lógica principal de gerenciamento dos treinos.
- `competicoes.py`: Lógica de gerenciamento de campeonatos e cálculo de datas.
- `agente_ia.py`: Integração com o LLM que faz a leitura dos dados.
- `utils.py` / `config.py`: Ferramentas de apoio e configurações globais.
- `menu.py` / `main.py`: Interface de navegação e ponto de entrada do sistema.
- `treinos.csv` / `competicoes.txt`: Arquivos locais que funcionam como o banco de dados do sistema.

---

## 👥 Contribuidores

<div align="center">

| [<img src="https://github.com/bryanmartins01.png" width="100" height="100" style="border-radius:50%">](https://github.com/bryanmartins01) | [<img src="https://github.com/felipeassiss.png" width="100" height="100" style="border-radius:50%">](https://github.com/felipeassiss) | [<img src="https://github.com/gabrielcrfp.png" width="100" height="100" style="border-radius:50%">](https://github.com/gabrielcrfp) | [<img src="https://github.com/gfva29.png" width="100" height="100" style="border-radius:50%">](https://github.com/gfva29) | [<img src="https://github.com/MourinhaJP.png" width="100" height="100" style="border-radius:50%">](https://github.com/MourinhaJP) | [<img src="https://github.com/leocadiok.png" width="100" height="100" style="border-radius:50%">](https://github.com/leocadiok) |
|:--:|:--:|:--:|:--:|:--:|:--:|
| **Bryan Martins** | **Felipe Assis** | **Gabriel Cassemiro** | **Gabriel Feitosa** | **João Pedro** | **Karla** |
</div>

<br>

---

## ⚙️ Como rodar o projeto

**OBS: É NECESSÁRIO TER O `git` E O `python` INSTALADOS NA SUA MÁQUINA.**

### 1. Primeira vez (Instalação e Configuração)

**Clonar o repositório:**
```bash
git clone https://github.com/felipeassiss/HyroxPlanner
```

### Entrar na pasta
```bash
cd HyroxPlanner
```

### Atualizar o projeto
```bash
git pull
```

### Após fazer alterações
```bash
git add .
git commit -m "descrição das alterações"
git push
```

---

# Após já ter clonado

### Atualizar o projeto
```bash
git pull
```

### Após fazer alterações
```bash
git add .
git commit -m "descrição das alterações"
git push
```
