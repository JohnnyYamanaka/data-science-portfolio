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
  * **GetData.py** - consome a API;
  * **VerificarDicionario.py**: Verifica se já existe o arquivo data_dictionary (caso já tenha rodado uma vez) e se sim sobreescreve o arquivo.
  * **salvar_arquivo.py**: Determina quais serão os indicadores para que o `GetData` possa consumir a API.

<br/>

* **requirements.txt**: arquivo txt contendo as dependências do projeto.

<br/>

* **notebooks**: pasta contendo os notebooks com a limpeza dos dados e as análises (em desenvolvimento).

<br/>

* **data_dictionary.txt**: arquivo contendo o dicionário de dados: código do indicador, seu significado e a sua unidade de medida.

___

## Prodecimento
Dentro do arquivo `salvar_arquivo.py`, defina quais são os indicadores desejados ([veja a lista de indicadores](https://servicodados.ibge.gov.br/api/docs/paises#api-acervo)) e preencha a lista indicadores.
Em seguida defina também os paises, seguindo a [norma ISO 3166-1 ALPHA-2](https://pt.wikipedia.org/wiki/ISO_3166-1_alfa-2). Feito isso, basta rodar esse arquivo para gerar os arquivos csv's com os dados brutos.
