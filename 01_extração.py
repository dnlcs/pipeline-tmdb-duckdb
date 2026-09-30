import requests
import json
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_bronze_pasta = os.path.join(diretorio_atual, "1_bronze")
os.makedirs(caminho_bronze_pasta, exist_ok=True)
caminho_bronze_arquivo = os.path.join(caminho_bronze_pasta, "filmes_populares.json")

todos_os_filmes = []

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMWJiOWI0NjQxMzcwYTI2MTYzNTQwZmMzNjhiOWI3OCIsIm5iZiI6MTc5MDI2MjgxNy43Nywic3ViIjoiNmFiNTNlMjFlZjg5Y2QzMDkwZmEwZjI3Iiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.QN3c7vnOEIYNT7VACBH7oCEj4IGXV3z980a_K065dBM" 
}

for pagina in range(1,21):
    url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={pagina}"
    resposta = requests.get(url, headers=headers)
    dados_brutos = resposta.json()
    todos_os_filmes.extend(dados_brutos['results'])
dados_finais = {"results": todos_os_filmes}

with open(caminho_bronze_arquivo, "w", encoding="utf-8") as arquivo:
    json.dump(dados_finais, arquivo, ensure_ascii=False, indent=4)

print(f"Extração concluída. Arquivo salvo em: {caminho_bronze_arquivo}")