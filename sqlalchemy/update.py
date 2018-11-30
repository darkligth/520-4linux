from sqlalchemy import update
from core import user_table, engine

con = engine.connect()

atlz = update(user_table).where(user_table.c.nome.like == 'teste1')

atlz = atlz.values(nome='Felipe Santos')

con.execute(atlz)