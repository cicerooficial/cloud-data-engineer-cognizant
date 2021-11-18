class Calculadora:
    # def __init__(self): #Não é obrigatório inicializar o método init já que já irá iniciar nada.
    #     pass

    def soma(self, valor_1, valor_2):
        return valor_1 + valor_2

    def subtracao(self, valor_1, valor_2):
        return valor_1 - valor_2

    def multiplicacao(self, valor_1, valor_2):
        return valor_1 * valor_2

    def divisao(self, valor_1, valor_2):
        return valor_1 / valor_2

calculadora = Calculadora()

print(calculadora.soma(10, 2))
print(calculadora.subtracao(5, 3))
print(calculadora.multiplicacao(10, 5))
print(calculadora.divisao(100, 2))


