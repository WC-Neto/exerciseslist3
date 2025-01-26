lista = ['Lucas', 'Walter', 'Roberto', 'Rafael', 'Luis', 'Marcio']
lista2 = list(filter(lambda nome: len(nome) > 5, lista))
print(lista2)
