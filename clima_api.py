import requests

API_KEY = "6b856f5f5c527205ba3689e1b60523b5"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def obter_clima(cidade):
    params = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt"
    }

    resposta = requests.get(BASE_URL, params=params)

    if resposta.status_code == 200:
        dados = resposta.json()
        nome = dados["name"]
        temp = dados["main"]["temp"]
        descricao = dados["weather"][0]["description"]
        print(f"\n Cidade: {nome}")
        print(f" Temperatura: {temp}°C")
        print(f" Clima: {descricao}")
    else:
        print("\n Cidade não encontrada. Tenta novamente.")

if __name__ == "__main__":
    print("=== Consulta de Clima ===")
    cidade = input("Digite o nome da cidade: ")
    obter_clima(cidade)