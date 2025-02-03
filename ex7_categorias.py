lista = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 0]
agrupados = dict()
positivos = list(filter(lambda x: x > 0, lista))
negativos = list(filter(lambda x: x < 0, lista))
neutro = list(filter(lambda x: x == 0, lista))
agrupados["positivos"] = positivos
agrupados["neutro"] = neutro
agrupados["negativos"] = negativos
print(agrupados)
