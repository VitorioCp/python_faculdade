class Veiculo:
    def __init__(self, nome, velocidade_maxima, km_por_litro):
        self.nome = nome
        self.velocidade_maxima = velocidade_maxima
        self.km_por_litro = km_por_litro
        
    def toStr(self):
        print(f'nome = {self.nome}')
        print(f'velocidade_maxima = {self.velocidade_maxima}')
        print(f'km_por_litro = {self.km_por_litro}')
        
modelo_carro = Veiculo("fusca", 180, 10)
modelo_carro.toStr()

class Onibus(Veiculo):
    def capacidade_assentos(self, capacidade=70):
        return capacidade
    
onibus_escolar = Onibus("Scania", 120, 8)
onibus_escolar.toStr()
print(f'capacidade_assentos = {onibus_escolar.capacidade_assentos()}')
