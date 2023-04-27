def somar_par(lst):
    soma = 0
    for num in lst:
        if num % 2 == 0:
            soma += num
    return soma

lista = [10, 2, 5, 7, 6, 3]
soma = somar_par(lista)
print(f'O somatório dos elementos pares é: {soma}')