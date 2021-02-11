from typing import List

def adicionarPilha(tamanho):
    addInfoPilha = str("")
    x = 0
    while x < tamanho:
        if equacao[x] == "(" or equacao[x] == ")":
            stack.append(equacao[x])
        elif equacao[x] == " ":
            if addInfoPilha != "":
                stack.append(addInfoPilha)
                addInfoPilha = str("")
        else:
            addInfoPilha += equacao[x]
            if x+1 == tamanho or equacao[x+1] == ")":
                stack.append(addInfoPilha)
                addInfoPilha = str("")
        x += 1

def calculandoValorNaPilha():
    camadaPrioridade = int(0)
    while 0 < len(stack):
        if len(stack) <= 1:
            break
        valorPilha = stack.pop()
        if valorPilha == ")":
            calculandoPilhaParentese(camadaPrioridade)
        else:
            valor2 = float(valorPilha)
            equacaoBasica(valor2, camadaPrioridade)

def equacaoBasica(valor2, camadaPrioridade):
    valorPilha = stack.pop()
    if valorPilha == str("/"):
        valorPilha = stack.pop()
        if valorPilha == ")":
            stackParentese.append("/")
            stackParentese.append(valor2)
            calculandoPilhaParentese(camadaPrioridade)
        else:
            valor1 = float(valorPilha)
            valor = valor1 / valor2
            stack.append(valor)
    elif valorPilha == str("*"):
        valorPilha = stack.pop()
        if valorPilha == ")":
            stackParentese.append("*")
            stackParentese.append(valor2)
            calculandoPilhaParentese(camadaPrioridade)
        else:
            valor1 = float(valorPilha)
            valor = valor1 * valor2
            stack.append(valor)
    elif valorPilha == str("+"):
        valorPilha = stack.pop()
        if valorPilha == ")":
            stackParentese.append("+")
            stackParentese.append(valor2)
            calculandoPilhaParentese(camadaPrioridade)
        else:
            valor1 = float(valorPilha)
            valor = valor1 + valor2
            stack.append(valor)
    elif valorPilha == str("-"):
        valorPilha = stack.pop()
        if valorPilha == ")":
            stackParentese.append("-")
            stackParentese.append(valor2)
            calculandoPilhaParentese(camadaPrioridade)
        else:
            valor1 = float(valorPilha)
            valor = valor1 - valor2
            stack.append(valor)


def calculandoPilhaParentese(camadaPrioridade):
    camadaPrioridade += 1
    while 0 < len(stack):
        valorPilha = stack.pop()
        if valorPilha == "(":
            valor2 = stackParentese.pop()
            stack.append(stackParentese.pop()) #+ - * /
            camadaPrioridade -= 1
            equacaoBasica(valor2, camadaPrioridade)
        elif valorPilha == ")":
            calculandoPilhaParentese(camadaPrioridade)
        else:
            valor2 = float(valorPilha)
            equacaoBasica(valor2, camadaPrioridade)
        if valorPilha == "(" and camadaPrioridade == 0:
            break;

def novoParentese(pilhaAberturaParentese, InformacaoParaAdicionarPilha, x, equacao, stackParentese, stack):
    x += 1
    pilhaAberturaParentese += 1
    while x < tamanho:
        if (equacao[x] == str("(")):
            return novoParentese(pilhaAberturaParentese, InformacaoParaAdicionarPilha, x, equacao, stackParentese, stack)
        elif (equacao[x] == str(")")):
            valor2 = float(stackParentese.pop())
            formulaUtilizada = stackParentese.pop()
            valor1 = float(stackParentese.pop())
            if formulaUtilizada == str("/"):
                valor1 = valor1 / valor2
            elif formulaUtilizada == str("*"):
                valor1 = valor1 * valor2
            elif formulaUtilizada == str("+"):
                valor1 = valor1 + valor2
            elif formulaUtilizada == str("-"):
                valor1 = valor1 - valor2
            stackParentese.append(float(valor1))
            print(stackParentese)
            pilhaAberturaParentese -= 1
            if pilhaAberturaParentese == 0:
                y = 0
                while len(stackParentese) >= y:
                    stackParentese.pop()
                    y += 1
                stack.append(float(valor1))
                return x
        elif (equacao[x] == str("-") and equacao[x+1] != str(" ")):
            InformacaoParaAdicionarPilha += equacao[x]
        elif (equacao[x] == str("/") or equacao[x] == str("*") or equacao[x] == str("+") or equacao[x] == str("-")):
            stackParentese.append(equacao[x])
        elif (equacao[x] != (" ") and equacao[x] != (")")):
            InformacaoParaAdicionarPilha += equacao[x]
            if equacao[x + 1] == str(" ") or equacao[x + 1] == str(")"):
                stackParentese.append(InformacaoParaAdicionarPilha)
                InformacaoParaAdicionarPilha = str("")


        x += 1

print("Adicione uma equacão para ser calculada.\nLembre-se de respeitar o espaço para fazer uma divisão entre numeros e ")
print("Lembre-se de respeitar os espaços!\nEx: (7.4 * 4) / ((2 − 1) − (4 / 3))\nEx: 2 + (5 * (−4 + 3))")
print("Aviso: Não copie e cole, escreva! Se não dá erro.")
equacao = str(input("Adicione a equação: "))
print(equacao)

#Pilha Principal
stack: List[str] = []

stackParentese: List[str] = []

#Variaveis
# x = 0
# pilhaAberturaParentese = 0
# valor1 = float(0)
# valor2 = float(0)
# novoValor = float(0)
# adquirindoValor2 = str("")
# InformacaoParaAdicionarPilha = str("")
# formulaNegativa = str("")

print("-----------------------------------")
print("-------- Folha de cálculo ---------")
print("-----------------------------------")
#Informação sendo totalmente salva na pilha
tamanho = len(equacao)
adicionarPilha(tamanho)
print("Pilha de toda equação salva: ")
print(stack)
calculandoValorNaPilha()
print(stack)

# while x < tamanho:
#     if (equacao[x] == str("-") and equacao[x + 1] != str(" ")):
#         while x < tamanho:
#             if (equacao[x] == str("-") or equacao[x] != str(" ")) and equacao[x] != str("("):
#                 formulaNegativa += equacao[x]
#             elif equacao[x] == str("("):
#                 x = novoParentese(pilhaAberturaParentese, InformacaoParaAdicionarPilha, x, equacao, stackParentese, stack)
#                 if formulaNegativa == "-":
#                     valorRetirado = float(stack.pop())
#                     novoValor -= valorRetirado
#                     stack.append(novoValor)
#                     novoValor = float(0)
#                     formulaNegativa = str("")
#                     print(stack)
#                 else:
#                     InformacaoParaAdicionarPilha = formulaNegativa
#                     if pilhaAberturaParentese >= 1:
#                         stack.append(InformacaoParaAdicionarPilha)
#                     else:
#                         stackParentese.append(InformacaoParaAdicionarPilha)
#                     print(stack)
#                     formulaNegativa = str("")
#                     print(stack)
#                     break
#             else:
#                 InformacaoParaAdicionarPilha = float(formulaNegativa)
#                 if pilhaAberturaParentese >= 1:
#                     stack.append(InformacaoParaAdicionarPilha)
#                 else:
#                     stackParentese.append(InformacaoParaAdicionarPilha)
#                 print(stack)
#                 formulaNegativa = str("")
#                 break
#             x += 1
#
#     elif (equacao[x] == str("+")):
#         valor1 = float(stack.pop())
#         while x < tamanho:
#             if (x + 1) > tamanho:
#                 break
#             elif (equacao[x] == "("):
#                 stack.append(valor1)
#                 x = novoParentese(pilhaAberturaParentese, InformacaoParaAdicionarPilha, x, equacao, stackParentese, stack)
#                 valor2 = float(stack.pop())
#                 valor1 = float(stack.pop())
#                 stack.append(valor1+valor2)
#                 print(stack)
#                 break
#             elif equacao[x] != str("/") and equacao[x] != str("*") and equacao[x] != str("+") and equacao[x] != str(
#                     "-"):
#                 if equacao[x] != str(" ") and equacao[x] != str(")"):
#                     adquirindoValor2 += equacao[x]
#                 if equacao[x] != str(" ") and (x + 1) == tamanho:
#                     valor2 = float(adquirindoValor2)
#                     InformacaoParaAdicionarPilha = float(valor1 + valor2)
#                     stack.append(InformacaoParaAdicionarPilha)
#                     InformacaoParaAdicionarPilha = str("")
#                     adquirindoValor2 = str("")
#                     print(stack)
#                     break
#                 elif equacao[x] != str(" ") and equacao[x + 1] == str(" "):
#                     valor2 = float(adquirindoValor2)
#                     InformacaoParaAdicionarPilha = float(valor1 + valor2)
#                     stack.append(InformacaoParaAdicionarPilha)
#                     InformacaoParaAdicionarPilha = str("")
#                     adquirindoValor2 = str("")
#                     print(stack)
#                     break
#             x += 1
#
#     elif (equacao[x] == str("-")):
#         valor1 = float(stack.pop())
#         while x < tamanho:
#             if (x + 1) > tamanho:
#                 break
#             elif (equacao[x] == "("):
#                 stack.append(valor1)
#                 print(stack)
#                 x = novoParentese(pilhaAberturaParentese, InformacaoParaAdicionarPilha, x, equacao, stackParentese,
#                                   stack)
#                 valor2 = float(stack.pop())
#                 valor1 = float(stack.pop())
#                 stack.append(valor1 - valor2)
#                 break
#             elif equacao[x] != str("/") and equacao[x] != str("*") and equacao[x] != str("+") and equacao[x] != str(
#                     "-"):
#                 if equacao[x] != str(" "):
#                     adquirindoValor2 += equacao[x]
#                 if equacao[x] != str(" ") and (x + 1) == tamanho:
#                     valor2 = float(adquirindoValor2)
#                     InformacaoParaAdicionarPilha = float(valor1 - valor2)
#                     stack.append(InformacaoParaAdicionarPilha)
#                     InformacaoParaAdicionarPilha = str("")
#                     adquirindoValor2 = str("")
#                     print(stack)
#                     break
#                 elif equacao[x] != str(" ") and equacao[x + 1] == str(" "):
#                     valor2 = float(adquirindoValor2)
#                     InformacaoParaAdicionarPilha = float(valor1 - valor2)
#                     stack.append(InformacaoParaAdicionarPilha)
#                     InformacaoParaAdicionarPilha = str("")
#                     adquirindoValor2 = str("")
#                     print(stack)
#                     break
#             x += 1
#
#     elif (equacao[x] == str("*")):
#         valor1 = float(stack.pop())
#         while x < tamanho:
#             if (x + 1) > tamanho:
#                 break
#             elif (equacao[x] == "("):
#                 stack.append(valor1)
#                 x = novoParentese(pilhaAberturaParentese, InformacaoParaAdicionarPilha, x, equacao, stackParentese, stack)
#                 valor2 = float(stack.pop())
#                 valor1 = float(stack.pop())
#                 stack.append(valor1*valor2)
#                 print(stack)
#                 break
#             elif equacao[x] != str("/") and equacao[x] != str("*") and equacao[x] != str("+") and equacao[x] != str(
#                     "-"):
#                 if equacao[x] != str(" "):
#                     adquirindoValor2 += equacao[x]
#                 if equacao[x] != str(" ") and (x + 1) == tamanho:
#                     valor2 = float(adquirindoValor2)
#                     InformacaoParaAdicionarPilha = float(valor1 * valor2)
#                     stack.append(InformacaoParaAdicionarPilha)
#                     InformacaoParaAdicionarPilha = str("")
#                     adquirindoValor2 = str("")
#                     print(stack)
#                     break
#                 elif equacao[x] != str(" ") and equacao[x + 1] == str(" "):
#                     valor2 = float(adquirindoValor2)
#                     InformacaoParaAdicionarPilha = float(valor1 * valor2)
#                     stack.append(InformacaoParaAdicionarPilha)
#                     InformacaoParaAdicionarPilha = str("")
#                     adquirindoValor2 = str("")
#                     print(stack)
#                     break
#             x += 1
#
#     elif (equacao[x] == str("/")):
#         valor1 = float(stack.pop())
#         while x < tamanho:
#             if (x + 1) > tamanho:
#                 break
#             elif (equacao[x] == "("):
#                 stack.append(valor1)
#                 x = novoParentese(pilhaAberturaParentese, InformacaoParaAdicionarPilha, x, equacao, stackParentese, stack)
#                 valor2 = float(stack.pop())
#                 valor1 = float(stack.pop())
#                 stack.append(valor1/valor2)
#                 print(stack)
#                 break
#             elif equacao[x] != str("/") and equacao[x] != str("*") and equacao[x] != str("+") and equacao[x] != str(
#                     "-"):
#                 if equacao[x] != str(" "):
#                     adquirindoValor2 += equacao[x]
#                 if equacao[x] != str(" ") and (x + 1) == tamanho:
#                     valor2 = float(adquirindoValor2)
#                     InformacaoParaAdicionarPilha = float(valor1 / valor2)
#                     stack.append(InformacaoParaAdicionarPilha)
#                     InformacaoParaAdicionarPilha = str("")
#                     adquirindoValor2 = str("")
#                     print(stack)
#                     break
#                 elif equacao[x] != str(" ") and equacao[x + 1] == str(" "):
#                     valor2 = float(adquirindoValor2)
#                     InformacaoParaAdicionarPilha = float(valor1 / valor2)
#                     stack.append(InformacaoParaAdicionarPilha)
#                     InformacaoParaAdicionarPilha = str("")
#                     adquirindoValor2 = str("")
#                     print(stack)
#                     break
#             x += 1
#
#     elif (equacao[x] == str("(")):
#         x = novoParentese(pilhaAberturaParentese, InformacaoParaAdicionarPilha, x, equacao, stackParentese, stack)
#         print(stack)
#         print(x)
#
#     elif (equacao[x] != str(" ")):
#         InformacaoParaAdicionarPilha += equacao[x]
#
#     elif (equacao[x] == str(" ")):
#         if InformacaoParaAdicionarPilha != "":
#             stack.append(float(InformacaoParaAdicionarPilha))
#             tamanhoStack += 1
#             print(stack)
#             InformacaoParaAdicionarPilha = str("")
#     x += 1
print("-----------------------------------")