import pandas as pd

dados = {
    "Nome": ["Nicolas", "Joao", "Paula", "Matheus", "Marta", "José", "Cleber"],
    "Idade": ["18","20","17","22","18","25","30"],
    "Local": ["São Paulo", "Recife", "Salvador", "Salvador", "Manaus", "Recife","Recife"]
}

df = pd.DataFrame(data=dados)

moradores_de_recife = df[df["Local"] == "Recife"]

print("Todos integrantes e suas cidades: ")
print(df)

print("Apenas moradores de Recife: ")
print(moradores_de_recife)

