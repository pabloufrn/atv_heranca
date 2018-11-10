class Veiculo:

    def __init__(self):
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def is_ligado(self):
        return self.ligado

class Automovel(Veiculo):

    def ligar(self):
        super(type(self), self).ligar()
        print(f"{type(self).__name__} está ligado.")

    def desligar(self):
        super(type(self), self).desligar()
        print(f"{type(self).__name__} está desligado.")

class Motocicleta(Veiculo):

    def ligar(self):
        super(type(self), self).ligar()
        print(f"{type(self).__name__} está ligada.")

    def desligar(self):
        super(type(self), self).desligar()
        print(f"{type(self).__name__} está desligada.")

class Onibus(Veiculo):

    def ligar(self):
        super(type(self), self).ligar()
        print(f"{type(self).__name__} está ligado.")

    def desligar(self):
        super(type(self), self).desligar()
        print(f"{type(self).__name__} está desligado.")

if(__name__ == "__main__"):
    carro = Automovel()
    moto = Motocicleta()
    busao = Onibus()

    carro.ligar()
    print(carro.is_ligado())
    carro.desligar()
    print(carro.is_ligado())

    moto.ligar()
    print(moto.is_ligado())
    moto.desligar()
    print(moto.is_ligado())

    busao.ligar()
    print(busao.is_ligado())
    busao.desligar()
    print(busao.is_ligado())
    
