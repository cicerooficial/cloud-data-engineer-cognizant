import shutil

# # parâmetro w escrve um arquivo. Caso o arquivo exista, irá sobrescrever.
# arquivo = open('teste.txt', 'w')
# arquivo.write('Minha primeira escrita')
# arquivo.close()
#
# # parâmetro a intera informação dentro do arquivo que já existe. Atualização
# arquivo = open('teste.txt', 'a')
# arquivo.write('\nMinha segunda escrita')
# arquivo.close()
#
# arquivo = open('teste.txt', 'a')
# arquivo.write('\nMinha terceira escrita')
# arquivo.close()

#Mesma coisa utilizando métodos
# def escrever_arquivo(texto):
#     arquivo = open('teste.txt', 'w')
#     arquivo.write(texto)
#     arquivo.close()


#Passando diretório como caminho para o open
def escrever_arquivo(texto):
    diretorio = 'C:/Users/cicer/Documents/GitHub/cloud-data-engineer-cognizant/9. Introducao-a-programacao-com-Python/app_python/teste.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

# def atualizar_arquivo(texto):
#     arquivo = open('teste.txt', 'a')
#     arquivo.write(texto)
#     arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n') #Toda vez que o método encontra o pâmetro passado, pegará a linha inteira como lista. Assim, conseguiremos acessar cada linha do registro.
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        #print(x)
        lista_notas = x.split(',')
        print(lista_notas)
        aluno = lista_notas[0]
        print(aluno)
        # print(sum(lista_notas)) #Erro pois está tudo como string. Para calculos é preciso converter para numérico
        lista_notas.pop(0) #Retirar a primeira posição da lista
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas)) #printar a media de cada aluno
        lista_media.append({aluno:media(lista_notas)}) #Incluir os resultados da linha acima em uma lista contendo cada aluno e sua respectiva média.
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/cicer/Documents/GitHub/cloud-data-engineer-cognizant/9. Introducao-a-programacao-com-Python/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/cicer/Documents/GitHub/cloud-data-engineer-cognizant/9. Introducao-a-programacao-com-Python/')

if __name__ == '__main__':
    #escrever_arquivo('Primeira linha. \n')
    #atualizar_arquivo('Seguneda linha. \n')
    #aluno = 'Claudio, 8, 9, 7, 5\n'
    # atualizar_arquivo('notas.txt',aluno)
    # ler_arquivo('teste.txt')
    #
    # lista_media = media_notas('notas.txt')
    # print(lista_media)

    copia_arquivo('notas.txt')
    move_arquivo('notas.txt')
