import requests

userCep = input('Digite o cep ai: ')

url = f'https://viacep.com.br/ws/{userCep}/json/'
r = requests.get(url)
cep = r.json()

print(cep)