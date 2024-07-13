time = input("Digite seu time: ")


# if time == 'Corinthians':
#     print("Você é um timao!")
# elif  time == "Bahia": 
#     print("Você é ddo Esquadrão!!")
# elif time == "Gremio": 
#     print("Você é um Imortal!")
# else:
#     print("Você não  é um timão")



match time:
    case "Corinthians":
        print("Você é um timão!")
    case "Bahia": 
        print("Você é Esquadrão!")
    case "Gremio":
        print("Você é um Imortal!") 
    case _: #"CASE _:" = "ELSE"
        print("Quem não é cai fora")
