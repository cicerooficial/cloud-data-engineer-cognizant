#TYratamento de erros

#ZeroDivisionError
# try:
#     divisao = 10/0
# except ZeroDivisionError:
#     print('Não é possível realizar um divisão por zero!')

#IndexError: list index out of range
# lista = [1, 10]
# try:
#     divisao = 10/1
#     numero = lista[3]
# except ZeroDivisionError:
#     print('Não é possível realizar um divisão por zero!')
# except:
#     print('Erro desconhecido')


# lista = [1, 10]
# try:
#     texto = arquivo.read()
#     divisao = 10 / 1
#     numero = lista[1]
#     x = a
# except ZeroDivisionError:
#     print('Não é possível realizar um divisão por zero!')
# except IndexError:
#     print('Erro desconhecido ao acessar o index da lista!')
# except BaseException as ex: #BaseException É o pai das exceptions(exceções), todo erro é BaseException qualquer outro erro cairá cair
#     print('Erro desconhecido. Erro: {}'.format(ex))
# else: #Executa quando não ocorre nenhuma exceção
#     print('Executa quando não ocorre exceção')


lista = [1, 10]
arquivo = open('C:/Users/cicer/Documents/GitHub/cloud-data-engineer-cognizant/9. Introducao-a-programacao-com-Python/app_python/teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    x = a
    print('Fechando arquivo')
    arquivo.close()
except ZeroDivisionError:
    print('Não é possível realizar um divisão por zero!')
except IndexError:
    print('Erro desconhecido ao acessar o index da lista!')
except BaseException as ex: #BaseException É o pai das exceptions(exceções), todo erro é BaseException qualquer outro erro cairá cair
    print('Erro desconhecido. Erro: {}'.format(ex))
else: #Executa quando não ocorre nenhuma exceção
    print('Executa quando não ocorre exceção')
finally: # Sempre executa o que tiver dentro do Finally, independente de erro ou exceção
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()
