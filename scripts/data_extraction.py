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
        response = requests.get(dados_empresa)
        if response.status_code==200:
            lista_empresas.append(response.json())
        else:
            print('falha ao obter dados')
    return lista_empresas

dados = con_data(cnpjs)


with open('empresas.json', 'w') as file:
    json.dump(dados, file, indent=4)