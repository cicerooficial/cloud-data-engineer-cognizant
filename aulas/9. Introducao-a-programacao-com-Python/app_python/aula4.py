# numero = int(input('Entre com o número: '))
#
# div = 0
#
# for x in range(1, numero+1):
#     resto = numero % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
# if div == 2:
#     print('número {} é primo'.format(numero))
# else:
#     print('número {} não é primio'.format(numero))


# loop = int(input('Entre com um numero primo: '))
#
# for numero in range(loop):
#     div = 0
#     for x in range(1, numero+1):
#         resto = numero % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print('{} é primo'.format(numero))


# a = 0
# while a <= 10:
#     print(a)
#     a +=1

nota1 = int(input('Nota do primeiro bimestre: '))
while nota1 > 10:
    nota1 = int(input('Você digitou a nota errada! '
          '\nNota do primeiro bimestre: '))
nota2 = int(input('Nota do segundo bimestre: '))
while nota2 > 10:
    nota2 = int(input('Você digitou a nota errada! '
          '\nNota do segundo bimestre: '))
nota3 = int(input('Nota do terceiro bimestre: '))
while nota3 > 10:
    nota3 = int(input('Você digitou a nota errada! '
          '\nNota do terceiro bimestre: '))
nota4 = int(input('Nota do quarto bimestre: '))
while nota4 > 10:
    nota4 = int(input('Você digitou a nota errada! '
          '\nNota do quarto bimestre: '))

media = (nota1+nota2+nota3+nota4) / 4

print('A média foi: {}'.format(media))

