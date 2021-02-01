listaSalario = []
listaFilhos = []
x = 0;
while x < 1:
    entrada = input().split(' ')
    salario = float(entrada[0])
    filhos = int(entrada[1])
    if salario < 0:
        break;
    else:
        listaSalario.insert(x, salario)
        listaFilhos.insert(x, filhos)
salarioTotal = 0
filhosTotal = 0
maiorSalario = 0
pessoasComBaixoSalario = 0
while x < len(listaSalario):
    if listaSalario[x] > maiorSalario:
        maiorSalario = listaSalario[x]
    if listaSalario[x] <= 2500:
        pessoasComBaixoSalario += 1
    salarioTotal += listaSalario[x]
    filhosTotal += listaFilhos[x]
    x += 1
pessoasComBaixoSalario = pessoasComBaixoSalario / len(listaSalario)
mediaSalario = salarioTotal / len(listaSalario)
mediaFilhos = filhosTotal / len(listaFilhos)

print(mediaSalario, mediaFilhos, maiorSalario, pessoasComBaixoSalario)