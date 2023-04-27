class Veiculo:
    def rodar(self):
        print("Reduz o cosnumo de combustivel.")


class VeiculoEletrico(Veiculo):
    def rodar(self):
        super().rodar()
        print("Esse veiculo utiliza eletricidade.")

veiculo_eletrico = VeiculoEletrico()
veiculo_eletrico.rodar()
