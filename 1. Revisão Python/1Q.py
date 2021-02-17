idadeVelho = int(0);
contador = int(0);
total = float(0);

while contador <= 100:
    idade = int(input("Adicione a idade: "));
    if idade > idadeVelho:
        idadeVelho = idade;
    elif idade == -1:
        print("Fim do While")
        break;
    lista = input("Adicione os 3 extras: ").split(' ');
    sexo = lista[0];
    cabelo = lista[1];
    olhos = lista[2];
    if sexo == "f":
        if (idade >= 18) and (idade <= 35):
            if cabelo == "l":
                if olhos == "v":
                    total += 1;
    contador += 1;

total = float((total * 100) / contador)

print("Mais Velho: %i" %idadeVelho)
print("Mulheres com olhos verdes, loiras com 18 a 35 anos: %.2f "%total)