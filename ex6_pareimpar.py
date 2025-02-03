lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, lista))
dict_pares = dict()
dict_pares["pares"] = pares
impares = list(filter(lambda x: x % 2 != 0, lista))
dict_impares = dict()
dict_impares["impares"] = impares
print(dict_pares, dict_impares)
