listaDobro = []
listaSoma = []
x = 0;
while x < 1:
    N = int(input())
    if N < 0:
        break;
    else:
        dobro = N * 2
        listaDobro.insert(x, dobro)
        y = 1
        soma = 0
        while y <= N:
            resto = N % y
            if resto == 0:
                soma += y
            y += 1
        listaSoma.insert(x, soma)
while x < len(listaSoma):
    dobro = listaDobro[x]
    soma = listaSoma[x]
    if dobro == soma:
        print("SIM")
    else:
        print("NAO")
    x += 1