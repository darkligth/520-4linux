from psycopg2 import  connect
from faker import Faker

fake = Faker('pt-br')

try:
    con = connect(
        "host=localhost user=python password=4linux dbname=fundamentals")
    cur = con.cursor()
    # cur.execute("select * from usuario")
    # print (cur.fetchone())
    for x in range(100):
        cur.execute("insert into usuario (nome, email, cpf, nascimento) values ('{}','{}','{}','{}')".format(fake.name(),fake.email(),fake.cpf(),fake.date_of_birth().strftime('%d-%m-%Y'))
        )
    con.commit()

except Exception as e:
    print(e)
    exit()
finally:
    try:
        cur.close()
        con.close()
    except Exception:
        print('Cursor nao definido!')
