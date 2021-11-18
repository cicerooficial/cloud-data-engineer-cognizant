a = 10
b = 5
soma = a+b
subtracao = a-b
multiplicacao = a*b
divisao = a/b
resto = a%b

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(resto)


print(type(soma))
print('soma: ' + str(soma))
print('subtracao' + str(subtracao))
print(int(divisao))

x= '1'
soma2 = int(x) + 1
print(soma2)

print('Soma: {}. Subtracao: {}'.format(soma, subtracao))
print('Soma: {soma}. Subtracao: {subtracao}'.format(soma=soma, subtracao=subtracao))
print('Soma: {soma}. '
      '\nSubtracao: {subtracao}. '
      '\nMultiplicacao: {multiplicacao}'.format(soma=soma,
                                                subtracao=subtracao,
                                                multiplicacao=multiplicacao))

a1 = int(input('Entre com o primeiro valor: '))
b1 = int(input('Entre com o segundo valor: '))

resultado = a1+b1
print('O resultado é: ' + resultado)