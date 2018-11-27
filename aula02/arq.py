#!/usr/bin/python3

# arquivo = open ('teste.txt', 'r')
# print(arquivo.readlines())
# arquivo.close()

# le as linhas do arquivo
#with open('teste.txt', 'r') as arquivo:
#    conteudo = arquivo.readlines()

#insere linha no arquivo
#with open('teste.txt', 'a') as arquivo:
#    arquivo.write('nova linha \n')
     
# conteudo  = 5*['novo\n']
# try:
#     with open ('teste1.txt', 'x') as arquivo:
#         for x in conteudo:
#             arquivo.write(x)
# except FileExistsError:
#     print ('arquivo ja existe')


with open('teste1.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()

with open('teste1.txt', 'w') as arquivo:
    cont = 1
    for x in conteudo:
        arquivo.write("{} - {}".format(cont, x))
        cont += 1
    



