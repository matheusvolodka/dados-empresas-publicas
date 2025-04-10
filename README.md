# Pipeline de dados de empresas
## Repositório para prática de ETL e Orquestração
Este repositório tem como objetivo a prática de uma pipeline que extraí dados de CNPJs e os salva no arquivo local
## Explicação
Na primeira variável `cnpjs` você pode colocar até 3 CNPJs de empresas diferentes para buscar os dados destas empresas.
A variável é uma lista que será iterada e criado um DataFrame, em seguida será salvo um arquivo CSV contendo informações relevantes
e um arquivo JSON contendo todas as informações das empresas selecionadas.

## Objetivos futuros
Com este projeto, quero criar um script em que você apenas selecione os cnpjs, e serão criados diretórios para cada empresa contendo suas informações separadas em um CSV e um JSON
## Preparação de ambiente
`python3 -m venv venv`  

`source venv/bin/activate`  

`pip install -r venv_req.txt`  

# Execução
`cd scripts && python3 data_extraction.py`