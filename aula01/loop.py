#!/usr/bin/python3
matriz = [
      [1,2,3],  
      [4,5,6],
      [7,8,9]
]
cont = 0
soma = 0
for m in matriz:
    soma += m[cont] + m[-(cont)]
    cont += 1

print (soma)
#soma = x.[0,0] + x[1,1] + x[2,2] + x[0,2] + x[1,1] + x[0,2]