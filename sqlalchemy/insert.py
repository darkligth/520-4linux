from core import user_table, engine

con = engine.connect()
#ins = user_table.insert()

#new = ins.values(nome='lucas', idade=28,senha='123456')
#print(str(new))

#con.execute(new)
con.execute(user_table.insert(),[
    {"nome": "teste1", 'idade':28, 'senha':'4linux'},
    {"nome": "teste2", 'idade':28, 'senha':'4linux'},
    {"nome": "teste3", 'idade':28, 'senha':'4linux'},
    {"nome": "teste4", 'idade':28, 'senha':'4linux'},
    {"nome": "teste5", 'idade':28, 'senha':'4linux'},
    {"nome": "teste6", 'idade':28, 'senha':'4linux'},
    {"nome": "teste7", 'idade':28, 'senha':'4linux'},

])