#"PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00
valor = float(input("Insira o valor total da compra: R$"))


# "O comando if sempre vai ser priorizado, então colocar o maior numero no if e o menor no elif"
if valor >= 500:
    print("PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%!!!")


elif valor >= 250:
    print("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")



else:
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")