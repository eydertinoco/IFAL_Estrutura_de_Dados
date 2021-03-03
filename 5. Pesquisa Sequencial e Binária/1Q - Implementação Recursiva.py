def descobrirRaiz(valorInteiro, y, media, mediaAnterior):
    if 0.000001 > ((media * media) - valorInteiro) > (-0.000001):
        print("A raiz de {} é igual a {}".format(valorInteiro, media))
        return media
    else:
        if (media*media) < valorInteiro:
            y = media
            media = (mediaAnterior+y)/2
            descobrirRaiz(valorInteiro, y, media, mediaAnterior)
        else:
            mediaAnterior = media
            media = (media+y)/2
            descobrirRaiz(valorInteiro, y, media, mediaAnterior)

valorInteiro = int(input("Adicione um valor inteiro positivo: "))
y = int(0)
mediaAnterior = int(0)
media = float(valorInteiro)
descobrirRaiz(valorInteiro, y, media, mediaAnterior)