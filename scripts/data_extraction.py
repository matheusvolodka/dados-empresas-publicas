import requests
import pandas as pd
import json


#Escolha os CNPJs das empresas da qual quer os dados
cnpjs = [
    '00000000000191', #BANCO DO BRASIL
    '33157312000162', #IFOOD
    '34075739000184'  #ESTÁCIO
]


#Conexão com a API e extração de dados
def con_dados(cnpj):
    lista_empresas = []
    for empresa in cnpj: 
        base_url = 'https://receitaws.com.br/v1/cnpj'
        dados_empresa = f'{base_url}/{empresa}'
        try:
            response = requests.get(dados_empresa, timeout=10)
            response.raise_for_status()
            lista_empresas.append(response.json())
        except requests.exceptions.HTTPError as http_err:
            print(f'Erro HTTP ao buscar CNPJ {empresa}: {http_err}')
        except requests.exceptions.ConnectionError:
            print(f'Erro de conexão ao buscar CNPJ {empresa}')
        except requests.exceptions.Timeout:
            print(f'Tempo de resposta esgotado para CNPJ {empresa}')
        except requests.exceptions.RequestException as err:
            print(f'Erro inesperado ao buscar CNPJ {empresa}: {err}')
    return lista_empresas

#Salva os dados num arquivo JSON, o parametro "nome_arquivo" é uma string com o formato do arquivo, ex: "empresas.json"
def salvar_json(dados, path_arquivo):
    with open(path_arquivo, 'w', encoding='utf-8') as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)

#Salva os dados num arquivo CSV, o parametro "nome_arquivo" é uma string com o formato do arquivo, ex: "empresas.csv"
def salvar_csv(dados, path_arquivo_csv):
    colunas = ['nome', 'cnpj', 'abertura', 'situacao', 'natureza_juridica', 'municipio', 'bairro', 'uf']
    df = pd.json_normalize(dados)
    df2 = pd.DataFrame(df)
    print(df2.head())
    return df[colunas].to_csv(path_arquivo_csv, index=False, encoding='utf-8')


#Execução do script

dados = con_dados(cnpjs)

salvar_json(dados, '../data/empresas.json')
salvar_csv(dados, "../data/empresas.csv")