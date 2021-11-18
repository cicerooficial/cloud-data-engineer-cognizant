# lista = [1, 3, 5, 7]
# lista_animais = ['cachorro', 'gato', 'elefante']
# print(lista, lista_animais)

# print(lista[2])
# print(lista_animais[1])
#
# for x in lista_animais:
#     print(x)
#
# soma = 0
# for y in lista:
#     print(y)
#     soma += y
# print(soma)
#
# print(sum(lista))
# print(max(lista))
# print(min(lista))
# print(max(lista_animais))   #letra em ordem alfabética de posição maior
# print(min(lista_animais))   #letra em ordem alfabética de posição menor
#
# if 'gato' in lista_animais:
#     print('Existe um gato na lista')
# else:
#     print('Não existe um gato na lista')
#
# if 'lobo' in lista_animais:
#     print('Existe um gato na lista')
# else:
#     print('Não existe um gato na lista')
#
# nova_lista = lista_animais * 3
# print(nova_lista)
#
# if 'lobo' in lista_animais:
#     print('Existe um gato na lista')
# else:
#     print('Não existe um gato na lista')
#     lista_animais.append('lobo')
#     print(lista_animais)

# lista_animais.pop()
# print(lista_animais)
# lista_animais.pop(1)
# print(lista_animais)
# lista_animais.remove('elefante')
# print(lista_animais)


# lista = [12, 10, 7, 5]
# lista_animais = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
# lista.sort()
# lista_animais.sort()
#
# print(lista)
# print(lista_animais)
#
# lista_animais.reverse()
# print(lista_animais)

lista = [12, 10, 7, 5]
lista_animais = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animais[0] = 'macaco'
print(lista_animais)

tupla = (1, 10, 12, 14)
print(tupla)
print(tupla[2])

# tupla[0] = 12 #Erro pois não é possível alterar valores da tupla. Tupla é imutável

print(len(tupla))
print(len(lista_animais))

tupla_animal = tuple(lista_animais)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)
lista_numerica[0] = 100
print(lista_numerica)

