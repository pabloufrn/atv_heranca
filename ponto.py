class Ponto2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x = {self.x}\ny = {self.y}"

class Ponto3d(Ponto2d):
    def __init__(self, x, y, z):
        super(type(self), self).__init__(x, y)
        self.z = z

    def __str__(self):
        return super(type(self), self).__str__() + f"\nz = {self.z}"

if(__name__ == "__main__"):
    p2d = Ponto2d(10, 20)
    print(p2d)
    p3d = Ponto3d(30, 40, 50)
    print(p3d)


