l = []
while True:
    nome = input("digite um nome para adicionar(digite não para sair) : ").upper()
    if nome == "não".upper():
        break
    l.append(nome)
l.sort(reverse=True)
x = 0
while x < len(l):
    print(l[x])

    x += 1
