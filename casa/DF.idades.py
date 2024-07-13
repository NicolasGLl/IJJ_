Idade = int(input("digite sua idade: "))


if Idade > 18:
 print("Legal! Você esta apto a dirigir!!")

elif Idade == 17 or Idade == 18:
 print("individuo tem entre 17 e 18 anos e ainda NÂO esta apto a dirigir")

else: 
 print("Você não esta apto a dirigir, por não ter a idade minima para dirigir")