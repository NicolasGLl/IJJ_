from faker import Faker


faker = Faker('pt_BR')


print(faker.name())

persona = {
    "nome": faker.name(),
    "cidade": faker.city(),
    "idade": faker.random_int(17, 80),

    
}

print(persona)

