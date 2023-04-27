class Pessoa:
    def _init_(self,nome,ender):
        self.set_nome(nome)
        self.set_ender(ender)
    
    def set_nome(self,nome):
        self.nome=nome

    def set_ender(self,ender):
        self.ender=ender
    
    def get_nome(self):
        return self.nome
    
    def get_ender(self):
        return self.ender
    
pessoa1 = Pessoa("Maria", "rua 01234")
pessoa2 = Pessoa("João", "rua 01234")

print(f'Nome: {pessoa1.get_nome()}, Endereço: {pessoa1.ender}')
        