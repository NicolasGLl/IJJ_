def verificacao_de_par_impar(numero) :
    if numero % 2 == 0:
        return "Você esta no time azul"
    else:
        return "Você esta no time amarelo"
    

numero_matricula = int(input("Digite o numero de sua matricula: "))
resultado = verificacao_de_par_impar(numero_matricula)

print(resultado)
