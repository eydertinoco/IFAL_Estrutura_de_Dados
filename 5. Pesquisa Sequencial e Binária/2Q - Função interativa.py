valorInteiro = int(input("Adicione um valor inteiro positivo: "))
y = int(0)
media = float(valorInteiro)

while (0 < valorInteiro):
    if 0.000001 > ((media * media) - valorInteiro) > (-0.000001):
        print("A raiz de {} é igual a {}".format(valorInteiro, media))
        break;
    else:
        if (media*media) < valorInteiro:
            y = media
            media = (mediaAnterior+y)/2
        else:
            mediaAnterior = media
            media = (media+y)/2