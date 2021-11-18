# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b:
#     print('O maior número é: {}'.format(a))
# else:
#     print('O maior número é: {}'.format(b))
# print('Final do programa!')
#
# if a > b and a > c:
#     print('O maior número é: {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é: {}'.format(b))
# else:
#     print('O maior número é: {}'.format(c))
# print('Final do programa!')


# a = int(input('Entre com o primeiro valor'))
# resto = a % 2
#
# if resto == 0:
#     print('O número é par')
# else:
#     print('O número é impar')
#
# a = int(input('Entre com o primeiro valor'))
# b = int(input('Entre com o segundo valor'))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
#     print('Foi digitado um número par')
# else:
#     print('nenhum número par foi digitado')
#
# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado um número par')
# else:
#     print('nenhum número par foi digitado')

nota1 = int(input('Nota do primeiro bimestre: '))
if nota1 > 10:
    print('Você digitou a nota errada! '
          '\nNota do primeiro bimestre: ')
nota2 = int(input('Nota do segundo bimestre: '))
if nota2 > 10:
    print('Você digitou a nota errada! '
          '\nNota do segundo bimestre: ')
nota3 = int(input('Nota do terceiro bimestre: '))
if nota3 > 10:
    print('Você digitou a nota errada! '
          '\nNota do terceiro bimestre: ')
nota4 = int(input('Nota do quarto bimestre: '))
if nota4 > 10:
    print('Você digitou a nota errada! '
          '\nNota do quarto bimestre: ')

media = (nota1+nota2+nota3+nota4) / 4

print('A média foi: {}'.format(media))

# if nota1<=10 and nota2<=10 and nota3<=10 and nota4<=10:
#     print('A média foi: {}'.format(media))
# else:
#     print('Foi informado alguma nota errada')

