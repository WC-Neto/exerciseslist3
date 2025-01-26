from functools import reduce
lista = [1, 2, 3, 5, 7, 11, 13, 17]
print(reduce(lambda x, y: x+y, lista))