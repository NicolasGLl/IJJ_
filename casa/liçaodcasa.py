linguagem_tupla = ('java' , 'python' , 'golang' , 'c#' , 'javascript')


linguagem_lista = list(linguagem_tupla)
print("tupla transformada em lista")

print(type(linguagem_lista))

#adicionando dois elementos com "extend"
linguagem_lista.extend({"ruby" , "malbolge"})
print("lista com dois dados adicionados")
print(linguagem_lista)

linguagem_lista.pop(0)


print("lista com JAVA removido")
print(linguagem_lista)

print("primeiro elemento:")
print(len(linguagem_lista))



dicionario = {
"nome": "Nicolas",
"idade": 18,
"profissão":"escravo de carteira assinada"
}

print("nome da pessoa: ", dicionario["nome"])
print("idade: ", dicionario["idade"])
print("profissao: ", dicionario["profissão"])