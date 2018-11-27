#!/usr/bin/python3

# def somar(x, y):
#     return x + y

# print (somar(4,4))    

# a = somar(4,3)
# b = somar(4,2)

# print (somar(a,b))


# def boas_vindas (nome='anonimo'):
#     return 'Seja bem vindo! '+nome

# print(boas_vindas())

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arq:
        return arq.readlines()

def escrever_arquivo(nome_arquivo, texto):
    with open(nome_arquivo, 'w') as arq:
        arq.writelines (texto)

def contar_linhas(nome_arquivo):
      return ler_arquivo(nome_arquivo).__len__()


print(ler_arquivo('shebang.py'))
escrever_arquivo('teste.txt', ler_arquivo('shebang.py'))
print(contar_linhas('shebang.py'))