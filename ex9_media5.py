lista = [(2, 8), (4, 5, 6), (1, 2)]
media5 = list(filter(lambda x: (sum(x)/len(x)) >= 5, lista))
print(media5)
