import requests

import GetData
import VerificarDicionario


indicadores = [77821, 77823, 77824, 77827,
               77831, 77832, 77833, 77849,
               77850, 77851]

#Dicionário com as siglas dos países seguindo a norma ISO 3166-1 alpha-2
#informações no link: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
paises = {'AR' : 'argentina', 'BO' : 'bolivia', 'BR' : 'brasil',
          'CL' : 'chile', 'CO' : 'colombia', 'EC' : 'equador',
          'GF' : 'guiana-francesa', 'PE' : 'peru', 'PY': 'paraguai',
          'SR' : 'suriname', 'UY' : 'uruguai', 'VE' : 'venezuela'}


dicionario = 'data_dictionary.txt'

# Verificar_dicionario()
VerificarDicionario.data_dictionary_exist(dicionario)
for indicador in indicadores:
    req = requests.get(
        f'https://servicodados.ibge.gov.br/api/v1/paises/indicadores/{indicador}'
    )

    VerificarDicionario.criar_dicionario_de_dados(req, indicador)


lista_chave_paises = list(paises.keys())

for count, pais in enumerate(paises):
    final_dict = {}
    for indicador in indicadores:
        print(pais, indicador)
        d = GetData.get_indicadores(lista_chave_paises[count], indicador)

        if bool(d):
            final_dict.update(d)
        else:
            pass

    print(f'o arquivo {pais} terá {len(final_dict.keys())} indicadores')
    print(f'sendo eles: {final_dict.keys()}')

    GetData.salvar_csv(final_dict, pais)
