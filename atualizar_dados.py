import os
import urllib.request
import csv
import json

# Puxa o link escondido do GitHub Secrets
url = os.environ.get("PLANILHA_URL")

if not url:
    raise ValueError("A variável PLANILHA_URL não foi encontrada!")

# Acessa a planilha e lê os dados
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
linhas = [linha.decode('utf-8') for linha in response.readlines()]

# Converte de CSV para JSON
leitor = csv.DictReader(linhas)
dados = list(leitor)

# Salva o arquivo dados.json na pasta do projeto
with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

print("Arquivo dados.json atualizado com sucesso!")
