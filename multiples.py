""" 
Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20. 
"""


def multiplos(num):
    rango = range(num+1)
    lista = []
    for numero in rango:
        if numero % 3 == 0 or numero % 5 == 0:
            lista.append(numero)
    lista = sum(lista)
    print(lista)


multiplos(num = 20)