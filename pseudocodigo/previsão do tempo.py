import requests

# Obter a chave da API da OpenWeatherMap
API_KEY = "58e865e67ac40b6523e9243e1fe82c9b"

# Obter a localização do usuário
cidade = input("Digite o nome da cidade: ")
pais = input("Digite o código do país: ")

# Montar a URL da API
link = f"http://api.openweathermap.org/data/2.5/weather?q={cidade},{pais}&appid={API_KEY}"

# Obter os dados do clima
resposta = requests.get(link)
dados_clima = resposta.json()

# Exibir as informações do clima
print(f"Clima em {cidade}, {pais}:")
print(f"Temperatura atual: {dados_clima['main']['temp']:.1f}°C")
print(f"Condições atuais: {dados_clima['weather'][0]['description']}")
print(f"Velocidade do vento: {dados_clima['wind']['speed']} km/h")
