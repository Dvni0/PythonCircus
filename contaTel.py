minutos = int(input(" Quantos minutos foram gastos por você: "))
if minutos < 200:
    preco = 0.2 * minutos
else:
    if minutos <= 400:
        preco = 0.18 * minutos
    else:
        preco = 0.15 * minutos
print(" o Preço que será pago por você será de R$%.2f" %preco)
