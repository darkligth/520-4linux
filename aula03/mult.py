class Pai:
    a = 'Classe pai'

class Mae:
    b = 'Classe mae'

class Filho (Pai, Mae):
    c = 'Classe filho'

objeto = Filho()

print(objeto.b, objeto.c)