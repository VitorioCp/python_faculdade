class Conta:
    def __init__(self, usuario, senha):
        self.senha = senha
        self.usuario = usuario
senha = 123
usuario = 'vitoriocp'
        
class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo, limite):
        super().__init__(clientes, numero, saldo)      
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor])
            return True

class Poupanca:
    def __init__(self, taxa_rendimento):
        self.taxa_rendimento = taxa_rendimento

    def remuneraConta(self):
        self.saldo += self.saldo * self.taxa_rendimento

class ContaRemuneradaPoupanca(Conta, Poupanca):
    def __init__(self, clientes, numero, saldo, taxaremuneracao):
        super().__init__(clientes, numero, saldo)
        Poupanca.__init__(self, taxaremuneracao / 30)
cx = ContaRemuneradaPoupanca([c1, c2], 98939123, 1500.00, 0.03)
cx.remuneraConta()
print(cx.saldo)

try:
    print(x)
except:
    print("Variavel indefinida")