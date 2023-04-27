class ClasseSomaMultiplica:
    def __init__(self,a,b):
         self.a = a
         self.b = b
    def somar(self):
         return self.a+self.b
    def multiplica(self):
         return self.a*self.b

class Derivado(ClasseSomaMultiplica):
    def subtrair(self):
          return self.a-self.b
    def Dividir(self):
         return self.a/self.b
    
d = Derivado(10,20)
print(f'A soma de 10 e 20: {d.somar()}')
print(issubclass(Derivado,ClasseSomaMultiplica))