quantNotaCem = 0
quantNotaCinq = 0
quantNotaDez = 0
quantNotaCinco = 0
quantNotaUm = 0
N = int(input())
x = 0
while x < 1:
    if N >= 100:
        quantNotaCem += 1
        N -= 100
    elif N >= 50:
        quantNotaCinq += 1
        N -= 50
    elif N >= 10:
        quantNotaDez += 1
        N -= 10
    elif N >= 5:
        quantNotaCinco += 1
        N -= 5
    else:
        quantNotaUm += 1
        N -= 1
    if N == 0:
        break;
while x < 1:
    if quantNotaCem > 0:
        print('{} nota(s) de R$ 100'.format(quantNotaCem))
    if quantNotaCinq > 0:
        print('{} nota(s) de R$ 50'.format(quantNotaCinq))
    if quantNotaDez > 0:
        print('{} nota(s) de R$ 10'.format(quantNotaDez))
    if quantNotaCinco > 0:
        print('{} nota(s) de R$ 5'.format(quantNotaCinco))
    if quantNotaUm > 0:
        print ('{} nota(s) de R$ 1'.format(quantNotaUm))
    x =+1