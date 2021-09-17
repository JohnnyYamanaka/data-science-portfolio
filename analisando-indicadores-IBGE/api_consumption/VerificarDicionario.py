import os

def data_dictionary_exist(file):
    file = file
    os.chdir('../')

    if os.path.exists(file):
        print('existe')
        os.remove(file)
        print('atualizando o arquivo')

    else:
        print('o arquivo nao existe')


def criar_dicionario_de_dados(req, indicador):
    data = req.json()
    key_values = [key for key in data[0].keys()]

    data_dictionary = dict(data[0].items())
    # data_dictionary.popitem()

    linhas = list()

    with open('./data_dictionary.txt', 'a') as file:
        for count, value in enumerate(key_values):
            if type(data_dictionary.get(value)) is dict:
                dict_in_dict = data_dictionary.get(value)
                linhas.append(f'unidade de medida - {dict_in_dict.get("id")} \n')

            else:
                linhas.append(f'{value} - {data_dictionary.get(value)} \n')

        file.writelines(linhas)
        file.writelines('\n')

        # return req
