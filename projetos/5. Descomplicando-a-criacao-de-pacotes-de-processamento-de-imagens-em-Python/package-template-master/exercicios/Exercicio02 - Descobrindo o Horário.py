"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada. Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horario = input('*** Digite apenas número de 0 à 23 ***\n'
                'Qual o horário?: ')

#Verifica se a variável está vazia
while horario == "":
    print('Tente digitar alguma coisa da próxima vez!\n')
    horario = input('*** Digite apenas número de 0 à 23 ***\n'
                    'Qual o horário?: ')

#Verifica se a variável é um número inteiro positivo
while not horario.isdigit():
    horario = input('*** Digite apenas número de 0 à 23 ***\n'
                    'Qual o horário?: ')

minutos = input('*** Digite apenas número de 0 à 60 ***\n'
                'Quantos minutos?: ')

#Verifica se a variável está vazia
while minutos == "":
    print('Tente digitar alguma coisa da próxima vez!\n')
    minutos = input('*** Digite apenas número de 0 à 60 ***\n'
                    'Quantos minutos?: ')

#Verifica se a variável é um número inteiro positivo
while not minutos.isdigit():
    minutos = input('*** Digite apenas número de 0 à 60 ***\n'
                'Quantos minutos?: ')

horario = int(horario)
minutos = int(minutos)

if horario > 23 or minutos > 60:
    print('Não foram digitados números de 0 à 23. Tente novamente! ')

if 0 <= horario <= 11:
    print(f'{horario}:{minutos} - Bom dia!')
elif 12 <= horario <= 17:
    print(f'{horario}:{minutos} - Boa tarde!')
elif 18 <= horario <= 23:
    print(f'{horario}:{minutos} - Boa noite!')

