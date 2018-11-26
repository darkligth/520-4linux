#!/usr/bin/python3
'''
lista = []
for x in range(97, 123):
    lista.append(chr(x))
print (lista)
'''
lista = [chr(x).upper() for x in range(97, 123) if chr(x) != 'a']
print(lista)