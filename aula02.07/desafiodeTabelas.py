import pandas as pd

dados = pd.read_csv(".\dados_ficticios.csv")

df = pd.DataFrame(data=dados)


print("pessoas com idade maior que 40 anos: ")
print(df[df["idade"] >46])


print("Pessoas com renda maior de 5 mil:  ")
print(df[df["renda"] >5000.00])


print("Pessoas com renda maior que 15mil:  ")
print(df[df["renda"] >15000.00])
