n = 1
soma = 0
while n <= 10:
    x = float(input(f"Digite o número {n}: "))
    soma += x
    n += 1

print(f"Soma = {soma:.2f}")
print(f"Soma = {(soma/10):.2f}")
