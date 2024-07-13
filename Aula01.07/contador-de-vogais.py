palavra = input("Por favor insira uma palavra: ")

contagem_vogais = 0 
vogais = "aeiouAEIOU"

for I in palavra: 
    if I in vogais: 
        contagem_vogais += 1

print(f"O numero total de vogais na palavra '{palavra}' é: {contagem_vogais}")