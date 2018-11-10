class Figura:

    def calcular_area(self):
        pass

class Quadrado(Figura):

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado**2

class Retangulo(Figura):

    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        return self.largura * self.altura

class FiguraComplexa(Figura):

    def __init__(self, figuras):
        self.figuras = figuras

    def calcular_area(self):
        return sum((figura.calcular_area() for figura in self.figuras))

if(__name__ == "__main__"):

    primeiro_quadrado = Quadrado(3)
    segundo_quadrado = Quadrado(10)

    primeiro_retangulo = Retangulo(2, 7)
    segundo_retangulo = Retangulo(5, 3)

    figura_complexa = FiguraComplexa([primeiro_quadrado, segundo_quadrado, primeiro_retangulo, segundo_retangulo])

    print("area total: ", figura_complexa.calcular_area())
