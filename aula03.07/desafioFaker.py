
from faker import Faker

fake = Faker("pt_BR")



def create_persona(number_of_personas: int): -> list: 
    personas_list = []

    for i in range(number_of_personas):
    data = {
    "nome": fake.name(),
    "cidade": fake.city(),
    "idade": fake.random_int(17, 100)
}
    personas_list.append(data)


return personas_list

#personas_list=[]

#for i in range(10):
#    personas_list.append(create_persona)

#persona_criada = create_persona()


#print(personas_list)




# def create_persona():

