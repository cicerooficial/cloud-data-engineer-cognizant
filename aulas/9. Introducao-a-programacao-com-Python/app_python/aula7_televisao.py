class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

# print(__name__)

if __name__ == '__main__': #Quem tiver chamando o método for o main(mesmo arquivo), ele faz os métodos abaixo, se for outro arquivo não faz nada.
    televisao = Televisao()
    print('Televisao está desligada!: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisao está ligada!: {}'.format(televisao.ligada))
    televisao.power()
    print('Televisao está desligada!: {}'.format(televisao.ligada))
    print('Canal: {}'.format(televisao.canal))
    televisao.power()
    print('Televisao está ligada!: {}'.format(televisao.ligada))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))
    televisao.power()
    print('Televisao está desligada!: {}'.format(televisao.ligada))