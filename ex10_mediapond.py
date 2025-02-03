'''Média ponderada com dicionário e reduce
Crie uma função que receba um dicionário onde as chaves são nomes de alunos e
os valores são listas de notas (com pesos na última posição). A função deve calcular
a média ponderada de cada aluno usando reduce e retornar um novo dicionário
com os resultados.
Exemplo de entrada:{
"João": [8, 7, 9, 2], # (notas: 8, 7, 9; peso: 2)
"Ana": [5, 6, 7, 3] # (notas: 5, 6, 7; peso: 3)
}
Exemplo de saída:
{
"João": 8.0,
"Ana": 6.0
}'''
from functools import reduce
turma = {"Walter": [6, 7, 8, 2], "Gyovana": [7, 8, 9, 3]}
valores = turma.values()
turma["Walter"] = reduce(lambda x, y: (
    x[0]*x[3]+x[1]*x[3]+x[2]*x[3])/(3*x[3]), valores)
turma["Gyovana"] = reduce(lambda x, y:(
    y[0]*y[3]+y[1]*y[3]+y[2]*y[3])/(3*y[3]) , valores)
print(turma)
