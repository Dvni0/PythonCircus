Numero1 = int(input("Digite um número inteiro: "))
Numero2 = int(input("Digite um segundo número inteiro: "))
Opera = input("digite um tipo de operação dentre as seguintes: Soma, Subtração, Multiplicação, "
              "Divisão: ")
if Opera  == "Soma":
    res = Numero1 + Numero2
elif Opera == "Subtração":
    res = Numero1 - Numero2
elif Opera == "Multiplicação":
    res = Numero1 * Numero2
elif Opera == "Divisão":
    res = Numero1 / Numero2
print(" o Resultado da operação escolhida com tais números é %.1f" %res)
