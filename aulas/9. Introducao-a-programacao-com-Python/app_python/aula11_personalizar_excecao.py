# try:
#     numero = int(input('Entre com um número de 0 a 10: '))
#     print(numero)
# except ValueError:
#     print('Valor inválido. Deve-se digitar apenas números.')


# while True:
#     try:
#         numero = int(input('Entre com um número de 0 a 10: '))
#         print(numero)
#         break
#     except ValueError:
#         print('Valor inválido. Deve-se digitar apenas números.')

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

    while True:
        try:
            numero = int(input('Entre com um número de 0 a 10: '))
            print(numero)
            if numero > 10:
                raise InputError('Nota não pode ser maior que 10') #Comando para forçar uma exceção
            elif numero < 0:
                raise InputError('Nota não pode ser menor que 0')
            break
        except ValueError:
            print('Valor inválido. Deve-se digitar apenas números.')
        except InputError as ex: #Aqui irá retornar a mensagem já tratada
            print(ex)
