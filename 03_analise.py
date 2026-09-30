import os
import duckdb

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_ouro_pasta = os.path.join(diretorio_atual, "3_ouro")
os.makedirs(caminho_ouro_pasta, exist_ok=True)

caminho_prata_arquivo = os.path.join(diretorio_atual, "2_prata", "filmes_limpos.csv").replace('\\','/')
caminho_ouro_arquivo = os.path.join(caminho_ouro_pasta, "indicadores_por_ano.csv").replace('\\','/')

query_ouro = f"""
SELECT
    EXTRACT(YEAR FROM CAST(data_lancamento AS DATE)) AS ano,
    COUNT(id) AS total_filmes,
    ROUND(AVG(nota_media),2) AS media_notas,
    ROUND(AVG(popularidade),2) AS media_popularidade
FROM read_csv_auto('{caminho_prata_arquivo}')
GROUP BY ano
ORDER BY ano DESC
"""

duckdb.query(f"COPY({query_ouro}) TO '{caminho_ouro_arquivo}' (HEADER, DELIMITER ',');")
print(f"Camada Ouro gerada em: {caminho_ouro_arquivo}")