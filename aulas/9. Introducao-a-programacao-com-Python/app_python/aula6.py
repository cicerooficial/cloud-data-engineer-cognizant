# conjunto = {1, 2, 3, 4}
# print(type(conjunto))
# print(conjunto)
#
# conjunto.add(5)
# print(conjunto)
# conjunto.discard(2)
# print(conjunto)

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto1.union(conjunto2)
print('Uniao: {}'.format(conjunto_uniao))

conjunto_interseccao = conjunto1.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))
conjunto_diferenca1 = conjunto1.difference(conjunto2)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
conjunto_diferenca2 = conjunto2.difference(conjunto1)
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))
conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2) #tudo que não tem relação entre os 2 conjuntos
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}
conjunto_subset1 = conjunto_a.issubset(conjunto_b) #Tem todo conjunto no outro conjunto
print(conjunto_subset1)
conjunto_subset2 = conjunto_b.issubset(conjunto_a)
print(conjunto_subset2)
conjunto_superset = conjunto_b.issuperset(conjunto_a) #Sempre que um conjunto for subconjunto de outro, esse outro é um superconjunto, pois tem todos os elementos do outro.
print(conjunto_superset)

#Converter lista para conjunto
lista = ['cachorro','cachorro','gato','gato','elefante']
conjunto_animais = set(lista)
print(conjunto_animais)

#Converter conjunto para lista
lista_animais = list(conjunto_animais)
print(lista_animais)