from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['projetos']

except Exception as  e:
    print(e)
    exit()

user = {'_id':5, "nome":"novo"}
db.usuario.insert(user)
db.usuario.update({},{ '$set':{'alunos.$.nome':'novonome','alunos.$.idade':'novaidade'}})

# busca = db.usuario.find_one({"_id":5})
# print(busca)

# busca = [x for x in busca]
# print(busca)
