import requests

# Entrada do usuário
cidade = input("Digite o nome da cidade: ")

# Chave da API (substitua pela sua)
api_key = "/9C4ghGVIQNO2TefHeSLSg==VxR8x3hWNOSLA4J7"

# URL da API com a cidade inserida
url = f"https://api.api-ninjas.com/v1/airquality?city={cidade}"
headers = {"X-Api-Key": api_key}

# Requisição GET à API
resposta = requests.get(url, headers=headers)

# Verifica se a requisição foi bem-sucedida
if resposta.status_code == 200:
    dados = resposta.json()

    print(f"\n   Qualidade do ar em {cidade.capitalize()}:")
    print(f" - Índice Geral (AQI): {dados['overall_aqi']}")
    print(f" - Partículas PM2.5: {dados['PM2.5']}")
    print(f" - Dióxido de Nitrogênio (NO2): {dados['NO2']}")
    print(f" - Ozônio (O3): {dados['O3']}")
else:
    print("  Não foi possível obter os dados. Verifique a cidade ou sua chave de API.")
