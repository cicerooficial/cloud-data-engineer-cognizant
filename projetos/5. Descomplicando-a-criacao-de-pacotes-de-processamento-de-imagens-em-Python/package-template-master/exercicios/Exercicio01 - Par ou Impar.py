"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro,
informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')

#Verifica se a variável está vazia
while numero == "":
    print('Tente digitar alguma coisa da próxima vez!\n')
    numero = input('Digite um número inteiro: ')

#Verifica se a variável é um número inteiro positivo
while not numero.isdigit():
    print('Não foi informado um número inteiro. Tente novamente! \n')
    numero = input('Digite um número inteiro: ')

numero = int(numero)

if numero % 2 == 0:
    print(f'O número {numero} é Par!')
else:
    print(f'O número {numero} é Impar!')
