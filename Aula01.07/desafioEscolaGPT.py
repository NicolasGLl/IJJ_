def verificar_par_impar(numero):
    if numero <= 0 or numero > 100:
        return "Número de matrícula inválido. Digite um número entre 1 e 100."
    elif numero % 2 == 0:
        return "VOCÊ ESTÁ NO TIME AZUL"
    else:
        return "VOCÊ ESTÁ NO TIME AMARELO"

# Exemplo de uso da função
while True:
    try:
        numero_matricula = int(input("Digite o número da matrícula (entre 1 e 100): "))
        resultado = verificar_par_impar(numero_matricula)
        print(resultado)
        break  # Sai do loop se a entrada foi válida e o resultado foi impresso
    except ValueError:
        print("Entrada inválida. Digite um número inteiro válido.")
