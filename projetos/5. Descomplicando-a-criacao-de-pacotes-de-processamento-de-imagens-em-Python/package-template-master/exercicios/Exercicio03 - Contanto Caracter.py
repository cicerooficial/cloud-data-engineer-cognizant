"""
Faça um programa que peça o primeiro nome do usuário.
Se o nometiver 4 letras ou menos escreva "Seu nome é curto";
Se tiver entre 5 e 6 letras, escreva "Seu nome é normal";
Se for maior que 6 letras, escreva "Seu nome é muito grande".
"""

nome = input('Digite seu primeiro nome: ')

#Verifica se a variável contém apenas string
while not nome.isalpha():
    print('Tente digitar apenas letras!')
    nome = input('Digite seu primeiro nome: ')

qtd_carater = len(nome)

if 0 < qtd_carater <= 4:
    print('Seu nome é curto!')
elif 5 <= qtd_carater <= 6:
    print('Seu nome é normal')
elif 6 < qtd_carater:
    print('Seu nome é muito grande')