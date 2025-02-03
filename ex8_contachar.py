from functools import reduce
lista = ['corinthians', 'campeão', 'esse', 'ano']
contador = list(map(lambda x: len(x), lista))
soma = reduce(lambda x, y: x+y, contador)
print(soma)
