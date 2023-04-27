preco_unitario = 10
DESCONTO10 = 0.1
DESCONTO20 = 0.2
quantidade = eval(input("digite o quantidade que você vai comprar: "))
if (quantidade <=10 ):
    valor_final = preco_unitario*quantidade
elif(quantidade <=20):
    valor_final = preco_unitario*quantidade*(1-DESCONTO10)
else:
    valor_final = preco_unitario*quantidade*(1-DESCONTO20)

print(f'O valor final da compra é de: {valor_final}')