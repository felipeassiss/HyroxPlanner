# HyroxPlanner

O **HyroxPlanner** é um sistema em Python criado para auxiliar no cadastro, visualização e organização de treinos HYROX, voltados para corrida, força e simulados.

O projeto foi desenvolvido com foco em praticar conceitos fundamentais de programação, como funções, dicionários, listas, entrada de dados, manipulação de datas e organização de código em módulos.

## Funcionalidades

- Cadastro de treinos
- Visualização de treinos cadastrados
- Busca de treino pelo nome
- Registro de informações como:
  - Nome do treino
  - Tipo do treino
  - Data
  - Duração
  - Intensidade

## Tecnologias utilizadas

- Python
- Biblioteca `datetime`

## Estrutura do treino

Cada treino cadastrado possui as seguintes informações:

```python
{
    "Nome": "Trote",
    "Tipo": "Corrida",
    "Data": "23/03/2026",
    "Duração": "01:30:00",
    "Intensidade": "leve"
}