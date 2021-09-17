# Análise de dados - Indicadores IBGE

--------

Projeto para adquirir dados de indicadores econômicos e sociais consumindo a API pública do IBGE ([veja a documentação da API aqui](https://servicodados.ibge.gov.br/api/docs/paises#api-_)), tratamento dos dados e posterior análise.  

___

## Depêndencias

Para conseguir rodar os arquivos do projeto são necessárias ter instaladas as bibliotecas básicas de ciência de dados, como pandas. Para tanto, basta executar o comando abaixo:
```
pip install -r requirements.txt
```
___

## Conteúdo

* **databases**: pasta contendo os arquivos .csv:
  * **[raw_data](./databases/raw_data)**: pasta os arquivos que foram adquirido, em seu  estado bruto;
  * **[processed](./databases/processed)**: pasta com os arquivos tratados.

<br/>

* **api_consumption**: pasta contendo os scripts em python para consumir a API:
  * **get_data.py** - consome a API.

<br/>

* **requirements.txt**: arquivo txt contendo as dependências do projeto.

<br/>

* **notebooks**: pasta contendo os notebooks com a limpeza dos dados e as análises (em desenvolvimento).

<br/>

* **data_dictionary.txt**: arquivo contendo o dicionário de dados: código do indicador, seu significado e a sua unidade de medida.
