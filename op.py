soma = 0
while True:
    num = (input("Digite um número a somar ou 'sair' para sair: "))
    num = int(num)
    if num == "sair":
     break
    soma += num
print(soma)
