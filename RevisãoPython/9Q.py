import math

x = int(0)
T = int(input())
while x < T:
    texto = input()
    tamanhoTexto = int(len(texto))
    n = math.sqrt(tamanhoTexto)
    print(tamanhoTexto)
    print("Raiz = ", n)
    y = int(0)
    z = int(0)
    while y <= n:
        if y == n:
            break;
        if z <= tamanhoTexto:
            lista.insert(z+0, texto[z])
        if (z+n+1) <= tamanhoTexto:
            lista.insert(z+n+1, texto[z+n+1])
        lista.
    y += 1
