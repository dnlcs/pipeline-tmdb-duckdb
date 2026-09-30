import os
import duckdb

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_prata_pasta = os.path.join(diretorio_atual, "2_prata")
os.makedirs(caminho_prata_pasta, exist_ok=True)

caminho_bronze_arquivo = os.path.join(diretorio_atual, "1_bronze", "filmes_populares.json").replace('\\', '/')
caminho_prata_arquivo = os.path.join(caminho_prata_pasta, "filmes_limpos.csv").replace('\\', '/')

query_limpeza = f"""
WITH filmes_brutos AS (
    SELECT unnest(results) AS film
    FROM read_json_auto('{caminho_bronze_arquivo}')
)
SELECT
    CAST(film.id AS INT) AS id,
    CAST(film.title AS VARCHAR) AS titulo,
    CAST(film.release_date AS DATE) AS data_lancamento,
    CAST(film.vote_average AS DOUBLE) AS nota_media,
    CAST(film.popularity AS DOUBLE) AS popularidade
FROM filmes_brutos
WHERE film.release_date IS NOT NULL
"""

duckdb.query(f"COPY({query_limpeza}) TO '{caminho_prata_arquivo}'(HEADER, DELIMITER ',');")
print(f"Limpeza concluída! Arquivo salvo em: {caminho_prata_arquivo}")

