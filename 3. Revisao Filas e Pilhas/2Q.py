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
            stackParentese.append(valor2)
            stackParentese.append("/")
            calculandoPilhaParentese(camadaPrioridade)
        else:
            valor1 = float(valorPilha)
            valor = valor1 / valor2
            stack.append(valor)
    elif valorPilha == str("*"):
        valorPilha = stack.pop()
        if valorPilha == ")":
            stackParentese.append(valor2)
            stackParentese.append("*")
            calculandoPilhaParentese(camadaPrioridade)
        else:
            valor1 = float(valorPilha)
            valor = valor1 * valor2
            stack.append(valor)
    elif valorPilha == str("+"):
        valorPilha = stack.pop()
        if valorPilha == ")":
            stackParentese.append(valor2)
            stackParentese.append("+")
            print("Valor estocado na Pilha Reserva: ")
            print(stackParentese)
            print("Valor atuais da Pilha: ")
            print(stack)
            calculandoPilhaParentese(camadaPrioridade)
        else:
            valor1 = float(valorPilha)
            valor = valor1 + valor2
            stack.append(valor)
    elif valorPilha == str("-"):
        valorPilha = stack.pop()
        if valorPilha == ")":
            stackParentese.append(valor2)
            stackParentese.append("-")
            calculandoPilhaParentese(camadaPrioridade)
        else:
            valor1 = float(valorPilha)
            valor = valor1 - valor2
            stack.append(valor)

def calculandoPilhaParentese(camadaPrioridade):
    camadaPrioridade += 1
    while 0 < len(stack):
        valorPilha = stack.pop()
        if len(stack) == 0 and valorPilha != "(":
            stack.append(valorPilha)
            break;
        if valorPilha == "(":
            valor2 = stackParentese.pop()
            stack.append(stackParentese.pop()) #+ - * /
            camadaPrioridade -= 1
            equacaoBasica(valor2, camadaPrioridade)
        elif valorPilha == ")":
            calculandoPilhaParentese(camadaPrioridade)
        else:
            condicaoFechamentoParentese = stack.pop()
            if condicaoFechamentoParentese == ("("):
                camadaPrioridade -= 1
                valor2 = valorPilha
                if len(stackParentese) > 0:
                    print("Invertendo a pilha para continuação do cálculo:")
                    while 0 < len(stackParentese):
                        stackParenteseInverso.append(stackParentese.pop())
                        print(stackParenteseInverso)
                    print("Fim da inversão.")
                    valorStackNumero = stackParenteseInverso.pop()
                    valorStackFator = stackParenteseInverso.pop()
                    if 0 < len(stackParenteseInverso):
                        print("Recolocando a pilha do paretense em ordem:")
                        while 0 < len(stackParenteseInverso):
                            stackParentese.append(stackParenteseInverso.pop())
                            print(stackParentese)
                        print("Fim da arrumação.")
                    stack.append(valor2)
                    valor2 = float(valorStackNumero)
                    stack.append(valorStackFator)
                else:
                    stack.append(valor2)
                    break;
                equacaoBasica(valor2, camadaPrioridade)
                print(stack)
            else:
                stack.append(condicaoFechamentoParentese)
                valor2 = float(valorPilha)
                equacaoBasica(valor2, camadaPrioridade)
                print(stack)
        if valorPilha == "(" and camadaPrioridade == 0:
            break;

print("Adicione uma equacão para ser calculada.")
print("Lembre-se de respeitar o espaço para fazer uma divisão entre numeros e de respeitar os espaços!")
print("Ex: (7.4 * 4) / ((2 − 1) − (4 / 3))\nEx: 2 + (5 * (−4 + 3))\nEx: -(3 * 4)")
print("------------- ATENÇÃO ----------------")
print("Não copie e cole, mas escreva todo a esquação!\nSe não vai dar erro de sintaxe!!")
print("---------------------------------------")
equacao = str(input("Adicione a equação: "))
print(equacao)

#Pilha Principal
stack: List[str] = []
#Pilha Complementar
stackParentese: List[str] = []
stackParenteseInverso: List[str] = []

print("-----------------------------------")
print("-------- Folha de cálculo ---------")
print("-----------------------------------")
#Informação sendo totalmente salva na pilha
tamanho = len(equacao)
adicionarPilha(tamanho)
print("Pilha de toda equação salva: ")
print(stack)
calculandoValorNaPilha()
valorFinal = str(stack.pop())
print("O valor final da equação é: " + valorFinal)
print("-----------------------------------")