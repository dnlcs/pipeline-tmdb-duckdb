# Pipeline ETL: Dados de Filmes (TMDB)

Este projeto implementa um fluxo de Engenharia de Dados local para extrair, transformar e analisar dados de filmes utilizando a API do TMDB. Toda a transformação de dados foi orquestrada com Python e processada através de consultas SQL utilizando o DuckDB.

## Arquitetura de Dados (Medalhão)

O pipeline está estruturado em três camadas lógicas:
* **Bronze**: Dados brutos em formato `.json` extraídos da rota de filmes populares da API do TMDB, com iteração de paginação.
* **Prata**: Dados higienizados, tipados e achatados (unnest) via consultas SQL no DuckDB. Foram selecionados campos essenciais (ID, título, data, nota e popularidade), filtrando registros sem data de lançamento e exportando para `.csv`.
* **Ouro**: Tabela agregada por ano de lançamento, contendo indicadores como total de filmes, média de notas e média de popularidade, gerada via DuckDB e pronta para consumo em BI.

## Tecnologias Utilizadas

* **Python**: Orquestração do pipeline, manipulação de diretórios e paginação.
* **Requests**: Biblioteca utilizada para o consumo e extração de dados via requisições HTTP na API do TMDB.
* **DuckDB**: Motor analítico utilizado para processar o JSON bruto, aplicar transformações estruturais com SQL (tipagem, unnest, agregações) e exportar os dados estruturados.

## Como reproduzir este projeto

1. Clone este repositório para a sua máquina:
```bash
git clone https://github.com/dnlcs/pipeline-tmdb-duckdb.git
```

2. Instale as bibliotecas necessárias:
```bash
pip install duckdb requests
```
3. Configuração da API:
Abre o ficheiro 01_extração.py e substitui o texto "SEU_TOKEN_AQUI" no cabeçalho pelo teu próprio Bearer Token da API do TMDB.

4. Execute os scripts pela ordem estrutural:
```bash
python 01_extração.py
python 02_limpeza.py
python 03_analise.py
```
