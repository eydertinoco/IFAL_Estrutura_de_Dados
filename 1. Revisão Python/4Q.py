N = int(input());
x = int(0);
nRepeticao = []
while x < N:
    texto = input().split(' ');
    numero = len(texto)
    y = int(0);
    repetidas = int(0);
    while y < numero:
        textoOriginal = texto[y]
        invertida = ' '.join(palavra[::-1] for palavra in texto[y].split())
        if textoOriginal == invertida:
            repetidas += int(1)
        y += 1
    nRepeticao.insert(x, repetidas)
    x += 1;
x = int(0);
while x < N:
    print(nRepeticao[x])
    x += 1;