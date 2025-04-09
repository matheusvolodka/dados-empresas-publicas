import requests
import pandas as pd
import json



cnpjs = [
    '00000000000191', #BANCO DO BRASIL
    '33157312000162', #IFOOD
    '34075739000184'  #ESTÁCIO
]


#Conexão com a API
def con_data(cnpj):
    lista_empresas = []
    for empresa in cnpj: 
        base_url = 'https://receitaws.com.br/v1/cnpj'
        dados_empresa = f'{base_url}/{empresa}'
        try:
            response = requests.get(dados_empresa, timeout=10)
            response.raise_for_status()  # Lança erro para códigos de status 4xx e 5xx
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


dados = con_data(cnpjs)
# df = pd.DataFrame(dados)
# print(df.head())

with open('empresas.json', 'w') as file:
    json.dump(dados, file, indent=4)