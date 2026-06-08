<div align="center">

  <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/dumbbell.svg" alt="HyroxPlanner Logo" width="80" height="80">

  # HyroxPlanner 🏋️‍♂️📊

  <br>

  ![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Groq](https://img.shields.io/badge/Groq-Powered-F55036?style=for-the-badge&logo=groq&logoColor=white)
  ![License](https://img.shields.io/badge/License-GPLv3-green?style=for-the-badge)
  <br>

</div>

---

O **HyroxPlanner** é um sistema de linha de comando **CLI**, desenvolvido em **Python**, criado para auxiliar no cadastro, visualização e organização de treinos HYROX, competições e simulações.

Além das funcionalidades tradicionais de gerenciamento de treinos, o projeto também conta com um assistente inteligente integrado à API da **Groq**, permitindo análises e respostas contextuais com base no histórico de treinos registrado.

---

## 🚀 Funcionalidades

### 🏋️ Domínio de Treinos (CRUD)

- Cadastrar novos treinos com nome, tipo, data, duração e intensidade
- Listar todos os treinos registrados
- Buscar treinos específicos pelo nome
- Editar dados de um treino existente
- Excluir treinos do registro

### 🏆 Domínio de Competições

- Cadastrar novas competições com nome, data e local
- Visualizar competições cadastradas
- Exibir contagem regressiva automática de dias até o evento

### 🤖 Assistente Inteligente com IA

- Integração com a API da Groq
- Uso de LLM para interpretar dados do histórico de treinos
- Respostas contextuais sobre desempenho, registros e evolução dos treinos

---

## 💻 Tecnologias e Bibliotecas Utilizadas

- **Python 3**
- **Groq API**
- **python-dotenv**
- Bibliotecas nativas:
  - `csv`
  - `os`
  - `datetime`

---

## 📁 Estrutura do Projeto

O código está organizado por **domínios de negócio**, facilitando a manutenção, leitura e evolução do projeto.

```bash
HyroxPlanner/
│
├── treinos.py          # Gerenciamento dos treinos
├── competicoes.py      # Gerenciamento das competições
├── agente_ia.py        # Integração com o assistente inteligente
├── utils.py            # Funções auxiliares
├── config.py           # Configurações globais
├── menu.py             # Interface de navegação
├── main.py             # Ponto de entrada do sistema
│
├── treinos.csv         # Base local de treinos
└── competicoes.txt     # Base local de competições
```
---

## 👥 Contribuidores

<div align="center">

| [<img src="https://github.com/brenomontenegro0508-droid.png" width="100" height="100" style="border-radius:50%">](https://github.com/brenomontenegro0508-droid) | [<img src="https://github.com/bryanmartins01.png" width="100" height="100" style="border-radius:50%">](https://github.com/bryanmartins01) | [<img src="https://github.com/felipeassiss.png" width="100" height="100" style="border-radius:50%">](https://github.com/felipeassiss) | [<img src="https://github.com/gabrielcrfp.png" width="100" height="100" style="border-radius:50%">](https://github.com/gabrielcrfp) | [<img src="https://github.com/GabrielFVA29.png" width="100" height="100" style="border-radius:50%">](https://github.com/gfva29) | [<img src="https://github.com/MourinhaJP.png" width="100" height="100" style="border-radius:50%">](https://github.com/MourinhaJP) | [<img src="https://github.com/leocadiok.png" width="100" height="100" style="border-radius:50%">](https://github.com/leocadiok) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| **Breno Montenegro** | **Bryan Martins** | **Felipe Assis** | **Gabriel Cassemiro** | **Gabriel Feitosa** | **João Pedro** | **Karla** |

</div>

<br>

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
