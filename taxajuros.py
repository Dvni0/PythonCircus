mes = 1
contador = 0

depinicial = float(input("Digite o deposito inicial: "))
taxajuros =  float(input("Digite a taxa de juros: "))
while mes <= 12:
    valormes = depinicial + depinicial * (taxajuros / 100)
    res =
    print(f" o Valor de deposito junto com os juros no mês {mes} é de {res}")
    contador = contador + res
    mes += 1


