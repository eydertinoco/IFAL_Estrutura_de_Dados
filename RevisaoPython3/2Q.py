from typing import List

def calculandoAplicando():
    x = 0
    tamanhoStack = 0
    valor1 = float(0)
    valor2 = float(0)
    adquirindoValor2 = str("")
    InformacaoParaAdicionarPilha = str("")
    formulaNegativa = str("")
    tamanho = len(equacao)
    while x < tamanho:
        if (equacao[x] == str("-") and equacao[x + 1] != str(" ")):
            while x < tamanho:
                if equacao[x] == str("-") or equacao[x] != str(" "):
                    formulaNegativa += equacao[x]
                else:
                    InformacaoParaAdicionarPilha = float(formulaNegativa)
                    stack.append(InformacaoParaAdicionarPilha)
                    print(stack)
                    formulaNegativa = str("")
                    break
                x += 1

        elif (equacao[x] == str("+")):
            valor1 = float(stack.pop())
            while x < tamanho:
                if (x + 1) > tamanho:
                    break
                elif equacao[x] != str("/") and equacao[x] != str("*") and equacao[x] != str("+") and equacao[x] != str(
                        "-"):
                    if equacao[x] != str(" "):
                        adquirindoValor2 += equacao[x]
                    if equacao[x] != str(" ") and (x + 1) == tamanho:
                        valor2 = float(adquirindoValor2)
                        InformacaoParaAdicionarPilha = float(valor1 + valor2)
                        stack.append(InformacaoParaAdicionarPilha)
                        InformacaoParaAdicionarPilha = str("")
                        adquirindoValor2 = str("")
                        print(stack)
                        break
                    elif equacao[x] != str(" ") and equacao[x + 1] == str(" "):
                        valor2 = float(adquirindoValor2)
                        InformacaoParaAdicionarPilha = float(valor1 + valor2)
                        stack.append(InformacaoParaAdicionarPilha)
                        InformacaoParaAdicionarPilha = str("")
                        adquirindoValor2 = str("")
                        print(stack)
                        break
                x += 1

        elif (equacao[x] == str("-")):
            valor1 = float(stack.pop())
            while x < tamanho:
                if (x + 1) > tamanho:
                    break
                elif equacao[x] != str("/") and equacao[x] != str("*") and equacao[x] != str("+") and equacao[x] != str(
                        "-"):
                    if equacao[x] != str(" "):
                        adquirindoValor2 += equacao[x]
                    if equacao[x] != str(" ") and (x + 1) == tamanho:
                        valor2 = float(adquirindoValor2)
                        InformacaoParaAdicionarPilha = float(valor1 - valor2)
                        stack.append(InformacaoParaAdicionarPilha)
                        InformacaoParaAdicionarPilha = str("")
                        adquirindoValor2 = str("")
                        print(stack)
                        break
                    elif equacao[x] != str(" ") and equacao[x + 1] == str(" "):
                        valor2 = float(adquirindoValor2)
                        InformacaoParaAdicionarPilha = float(valor1 - valor2)
                        stack.append(InformacaoParaAdicionarPilha)
                        InformacaoParaAdicionarPilha = str("")
                        adquirindoValor2 = str("")
                        print(stack)
                        break
                x += 1

        elif (equacao[x] == str("*")):
            valor1 = float(stack.pop())
            while x < tamanho:
                if (x + 1) > tamanho:
                    break
                elif equacao[x] != str("/") and equacao[x] != str("*") and equacao[x] != str("+") and equacao[x] != str(
                        "-"):
                    if equacao[x] != str(" "):
                        adquirindoValor2 += equacao[x]
                    if equacao[x] != str(" ") and (x + 1) == tamanho:
                        valor2 = float(adquirindoValor2)
                        InformacaoParaAdicionarPilha = float(valor1 * valor2)
                        stack.append(InformacaoParaAdicionarPilha)
                        InformacaoParaAdicionarPilha = str("")
                        adquirindoValor2 = str("")
                        print(stack)
                        break
                    elif equacao[x] != str(" ") and equacao[x + 1] == str(" "):
                        valor2 = float(adquirindoValor2)
                        InformacaoParaAdicionarPilha = float(valor1 * valor2)
                        stack.append(InformacaoParaAdicionarPilha)
                        InformacaoParaAdicionarPilha = str("")
                        adquirindoValor2 = str("")
                        print(stack)
                        break
                x += 1

        elif (equacao[x] == str("/")):
            valor1 = float(stack.pop())
            while x < tamanho:
                if (x + 1) > tamanho:
                    break
                elif equacao[x] != str("/") and equacao[x] != str("*") and equacao[x] != str("+") and equacao[x] != str(
                        "-"):
                    if equacao[x] != str(" "):
                        adquirindoValor2 += equacao[x]
                    if equacao[x] != str(" ") and (x + 1) == tamanho:
                        valor2 = float(adquirindoValor2)
                        InformacaoParaAdicionarPilha = float(valor1 / valor2)
                        stack.append(InformacaoParaAdicionarPilha)
                        InformacaoParaAdicionarPilha = str("")
                        adquirindoValor2 = str("")
                        print(stack)
                        break
                    elif equacao[x] != str(" ") and equacao[x + 1] == str(" "):
                        valor2 = float(adquirindoValor2)
                        InformacaoParaAdicionarPilha = float(valor1 / valor2)
                        stack.append(InformacaoParaAdicionarPilha)
                        InformacaoParaAdicionarPilha = str("")
                        adquirindoValor2 = str("")
                        print(stack)
                        break
                x += 1

        elif (equacao[x] == str("(")):
            while x < tamanho:


                pilhaAberturaParentese = []

                if equacao[x] == ")":
                    break;
                x += 1

        elif (equacao[x] != str(" ")):
            InformacaoParaAdicionarPilha += equacao[x]

        elif (equacao[x] == str(" ")):
            if InformacaoParaAdicionarPilha != "":
                stack.append(float(InformacaoParaAdicionarPilha))
                tamanhoStack += 1
                print(stack)
                InformacaoParaAdicionarPilha = str("")
        x += 1


print("Adicione uma equacão para ser calculada.\nLembre-se de respeitar o espaço para fazer uma divisão entre numeros e ")
equacao = str(input("Adicione a equação: "))
print(equacao)
stack: List[str] = []

stackParentese: List[str] = []

print("-----------------------------------")
print("-------- Folha de cálculo ---------")
print("-----------------------------------")
calculandoAplicando()
print("-----------------------------------")