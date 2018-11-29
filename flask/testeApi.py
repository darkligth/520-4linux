#import requests, json
from faker import Faker
from conect import mongo_connect

fake = Faker('pt-br')
db = mongo_connect('projetos')

for x in range(1000):
    data = {
        "_id":x,
        "nome": fake.name(),
        "email": fake.email(),
        "cpf": fake.cpf(),
        "nascimento": fake.date_of_birth().strftime('%d-%m-%Y')
    }
    db.usuario.insert(data)


# re = requests.get('https://viacep.com.br/ws/0500100/json/')
# print(re.json)

# headers = {"content-type":"application/json"}
# data = {"nome":"Felipe", "idade":"28"}

# re = requests.post(
#     "http://127.0.0.1:5000/",
#     data=data,
# #   headers=headers
# )
# #print(re.json())