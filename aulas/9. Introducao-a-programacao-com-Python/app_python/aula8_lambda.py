#lambda é uma função anônima. É uma forma de simplificar alguma coisa que utilizamos mais de uma vez no código
#Obs.: Usar somente para funções que é possível resolver em uma linha. FUnções complexas não é indicado.
#Vamos simplificar a o contador de letras
# def contador_letras(lista_palavras):
#     contador = []
#     for x in lista_palavras:
#         quantidade = len(x)
#         contador.append(quantidade)
#     return contador

contador_letras = lambda lista: [len(x) for x in lista] #Função anônima

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
multiplicacao = lambda a, b: a * b
divisao = lambda a, b: a / b

print(soma(5, 10))
print(subtracao(10, 5))
print(multiplicacao(3, 7))
print(divisao(100, 2))

#Dicionario com lambda
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora))

soma = calculadora['soma'] # É a mesma coisa que soma = lambda a, b: a + b
print('A soma é: {}'.format(soma(10, 5)))

subtracao = calculadora['subtracao']
print('A subtracao é: {}'.format(subtracao(10, 5)))

multiplicacao = calculadora['multiplicacao']
print('A subtracao é: {}'.format(multiplicacao(3, 7)))

divisao = calculadora['divisao']
print('A divisao é: {}'.format(divisao(100, 2)))

