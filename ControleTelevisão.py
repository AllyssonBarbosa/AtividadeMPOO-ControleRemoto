class Televisao:
    def __init__(self) :
        self.canal = 1
        self.volume = 10
        self.ligada = False

    def ligarDesligar(self):
        if self.ligada == False:
            self.ligada = True
            print("A televisão foi ligada")
        elif self.ligada == True:
            self.ligada = False
            print("A televisão foi desligada")

    def aumentarVolume(self):
        if self.volume < 20:
            self.volume += 1
            print("Volume atual: ", self.volume)
        else:
            print("A televisão esta no volume máximo")

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
            print("Volume atual: ", self.volume)
        else:
            print("A televisão está no mudo")

    def mutarVolume(self):
        if self.volume > 0 :
            self.volume = 0
            print("A televisão está no mudo")

    def aumentarCanal(self):
        if self.canal < 99:
            self.canal += 1
            print("O canal atual é: ", self.canal)
        elif self.canal == 99:
            self.canal = 1
            print("O canal atual é: ", self.canal)

    def diminuirCanal(self):
        if self.canal > 1:
            self.canal -= 1
            print("O canal atual é: ", self.canal)
        elif self.canal == 1:
            self.canal = 99
            print("O canal atual é: ", self.canal)
    
    def selecionarCanal(self, numCanal):
        self.canal = numCanal
        print("A televisão esta no canal: ", self.canal)
    

tv = Televisao()
tv.aumentarVolume()
tv.aumentarCanal()
tv.aumentarCanal()
tv.mutarVolume()
tv.diminuirCanal()
tv.diminuirVolume()
tv.selecionarCanal(22)
tv.diminuirCanal()

