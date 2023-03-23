import math 
class Punto():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
    def coordenada(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante" 
        elif self.x == 0 and self.y != 0:
            return "El punto esta sobre el eje de las X"
        elif self.x != 0 and self.y == 0:
            return "El punto esta sobre el eje de las Y"
        else:
            return "Punto de origen"
    def vector(self,p2):
        return "El vector es: " f'({abs(self.x - p2.x)},{abs(self.y - p2.y)})'
    def distancia(self,p2):
        return "La dist es: " f'{math.sqrt((abs(self.x - p2.x)**2) + abs(self.y - p2.y)**2)}'
class Rectangulo(Punto):
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    def base(self):
        return "La base es igual a: " f'{abs(self.p1.x - self.p2.x)}' 
    def altura(self):
        return "La altura es igual a:" f'{abs(self.p1.y - self.p2.y)}'
    def area(self):
        return "El area es igual a:" f'{(self.p1.x - self.p2.x) * (self.p1.y - self.p2.y)}'
    def rectangulo(self):
        return "las coordenadas del rectángulo que faltan son: C" f'{self.p1.x}'
def main():
    A = Punto(2,3)
    B = Punto(5,5)
    C = Punto(-3,-1)
    D = Punto(0,0)
    print(A)
    print(B)
    print(A.coordenada())
    print(C.coordenada())
    print(D.coordenada())
    print(A.vector(B))
    print(B.vector(A))
    print(A.distancia(B))
    print(B.distancia(A))
    if A.distancia(D) > B.distancia(D) and A.distancia(D) > C.distancia(D):
        return ("A es el más cercano a D")
    if B.distancia(D) > A.distancia(D) and B.distancia(D) > C.distancia(D):
        print("B es el más cercano a D")
    else:
        return ("C es el más cercano a D")
    rectangulo = Rectangulo(A,B)
    print(rectangulo.base())
    print(rectangulo.altura())
    print(rectangulo.area())
    print(rectangulo.rectangulo())
if __name__ == "__main__":
    main()
        
    
        