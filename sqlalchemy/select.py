from sqlalchemy import select
from core import user_table

slct = select([user_table])

print (list(slct.execute()))

for registro in slct.execute():
    print(registro)