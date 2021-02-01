N = int(input());
if (N >= 1) and (N <= 1000):
    texto = input().split(' ');
    x = int(0);
    posicao = int(0);
    valorMenor = int(1000);
    while x < N:
        valor = int(texto[x])
        if valor < valorMenor:
            valorMenor = valor
            posicao = x;
        x += 1;
    print("Menor Valor:", valorMenor)
    print("Posicao:", posicao)