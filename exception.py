class ExcecaoCustumizada(Exception):
    pass
x = -1
if x <0:
    raise Exception("Valor negativo !!!")

x ="Hello"
if not type(x) is int:
    raise TypeError("User apenas inteiros")