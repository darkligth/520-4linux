#!/usr/bin/python3
'''
try:
    nota1 = float (input('digite a primeira nota: '))
    nota2 = float (input('digite a segunda nota: '))
except Exception as e:
    print('Erro: %s' % e)
    exit()
'''
qtdNotas = int(input('Digite a quantidade de notas para avaliar'))

media = 0

for x in range(qtdNotas):
    media += float(input('digite a uma nota:'))
    

media = media / qtdNotas

if media  >= 7:
    result = 'aprovado'
elif media > 3:
    result = 'recuperacao'
else:
    result = 'reprovado'

print ('resultado : {} media: {}'.format(result, media))