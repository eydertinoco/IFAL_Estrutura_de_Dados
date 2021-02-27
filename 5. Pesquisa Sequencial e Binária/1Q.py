x = int(input("Adicione um valor inteiro positivo: "))
y = int(0)
media = float(x/2)

while (0 < x):
    if ((media * media) - x) < 0.000001 and ((media * media) - x) > (-0.000001):
        print("A raiz de {} é igual a {}".format(x, media))
        break;
    else:
        if (media*media) < x:
            y = media
            media = (mediaAnterior+y)/2
        else:
            mediaAnterior = media
            media = (media+y)/2