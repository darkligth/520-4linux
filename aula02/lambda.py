#!/usr/bin/python3
a  = lambda x: x + 2

# print(a(2))
#print((lambda x: x + 2)(5))

[(lambda x: x + 2)(y) for y in range(1)]

#print([(lambda x: x * x )(y) for y in range(2,12)])

a = list (map(lambda y: y **2, range(1,11)))
print (a)