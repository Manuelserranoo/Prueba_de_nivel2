import math 
class Punto():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
    def sum(self):
        return self.x + self.y
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
        return "La dist es: " f'({math.sqrt((abs(self.x - p2.x)**2) + abs(self.y - p2.y)**2)})'
    
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
if __name__ == "__main__":
    main()
        
    
        