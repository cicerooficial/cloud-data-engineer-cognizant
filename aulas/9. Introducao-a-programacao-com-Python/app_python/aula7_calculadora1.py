# Função - Tudo que retorna um valor
# Método - Tudo que não retorna um valor.
# No python os métodos não são explícitos, métodos são chamados de def (definição),
# caso aja um return, passa a ser uma função.

# def soma(a, b):
#     return a + b
#
# print(soma(1, 2))
# print(soma(3, 4))
#
# def subtracao(a, b):
#     return a - b
#
# print(subtracao(10, 2))
#
# def multiplicacao(a, b):
#     return a * b
#
# print(multiplicacao(10, 2))
#
# def divisao(a, b):
#     return a / b
#
# print(divisao(10, 2))


#Classe -

class Calculadora:
    def __init__(self, num1, num2): #Incluindo o init, self, sempre que a classe for iniciada ele irá executar o init primeiramente. E toda variável to self deve ser refenciada nos métodos.
        self.valor_1 = num1
        self.valor_2 = num2

    def soma(self):
        return self.valor_1 + self.valor_2

    def subtracao(self):
        return self.valor_1 - self.valor_2

    def multiplicacao(self):
        return self.valor_1 * self.valor_2

    def divisao(self):
        return self.valor_1 / self.valor_2


if __name__ == '__main__':
    calculadora = Calculadora(10, 2)
    print(calculadora.valor_1)
    print(calculadora.valor_2)

    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())
