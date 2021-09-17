import requests
import os
import json
import pandas as pd

def get_indicadores(pais, indicador):
    req = requests.get(
        f'https://servicodados.ibge.gov.br/api/v1/paises/{pais}/indicadores/{indicador}')

    #Transformando o content numa lista de json e acessando ela.
    #Repetir esse processo até chegar ao valor 'serie', onde estão
    #o dicionario com os anos e o valor do indicador.
    data = req.json()
    dict_data = data[0]

    if len(dict_data.get('series')) == 0:
        pass

    else:
        dict_series = (dict_data.get('series')[0])

        #Lista de dicionarios onde estão as informações desejadas {ano : valor}
        serie = dict_series['serie']


        #Criar as listas para guardar as chaves (ano) e valores (do indicador)
        #e percorrer a lista de dicionario e retirar o primeiro valor, que é
        #uma linha vazia.
        list_of_keys = list()
        list_of_values = list()

        #Filtro para reg
        for key in range(len(serie)):
            if list(serie[key].keys())[0] == '-':
                pass

            else:
                list_of_keys.append(list(serie[key].keys())[0])

        for item in range(len(serie)):
            list_of_values.append(list(serie[item].values())[0])

        #Retirar da lista valores o primeiro item, referente a chave do primeiro
        #item da lista "-"
        list_of_values.pop(0)

        #Dicionario contendo o resultado
        d = {'year' : list_of_keys, f'cod_{indicador}' : list_of_values}

        return d
        # final_dict = {}
        # final_dict.update(d)
        #
        # # df = pd.DataFrame(final_dict)
        # # df.to_csv(f'./databases/raw_data/indicadores_{pais}.csv', index=False)
        #
        # return final_dict

def salvar_csv(final_dict, pais):
    df = pd.DataFrame(final_dict)
    df.to_csv(f'./databases/raw_data/indicadores_{pais}.csv', index=False)
