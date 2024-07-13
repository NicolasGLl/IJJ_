import pandas as pd


dados = {
    "Nome": ["Joao", "Marta", "Ary", "Matheus", "Michelle"],
    "Idade": [51,37,23,24,33]
}

df = pd.DataFrame(data=dados)

print(df)
