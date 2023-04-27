#Método Classe
""""
class NomeCompleto:
    def __init__(self,nome,sobrenome) :
        self.nome = nome
        self.sobrenome = sobrenome
    @classmethod
    def fromString(cls,texto):
        nome, sobrenome = map(str, texto.split(' '))
        objeto = cls(nome,sobrenome)
        return objeto
    
registro1 = NomeCompleto.fromString("Luiz Braga")
"""
#Método estático
class NomeCompleto:
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    @classmethod
    def fromStreng(cls,texto):
        nome, sobrenome = map(str, texto.slit(' '))
        objeto = cls(nome,sobrenome)
        return objeto
    @staticmethod
    def isValid(texto):
        nomes = texto.split(' ')
        return len(nomes) > 1
        
