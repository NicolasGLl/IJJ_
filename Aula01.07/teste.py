import requests


cep = input("qual seu CEP: ")

response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")


data = response.json()

print(f"o logradouro dessa chamada é: ", data ["logradouro"])