#!/usr/bin/python3

nota1 = input('digite a primeira nota: ')
nota2 = input('digite a segunda nota: ')

media = (float(nota1) + float(nota2)) / 2

if media  >= 7:
    result = 'aprovado'
elif media > 3:
    result = 'recuperacao'
else:
    result = 'reprovado'

print ('resultado : {} media: {}'.format(result, media))