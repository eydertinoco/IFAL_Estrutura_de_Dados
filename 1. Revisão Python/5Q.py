x = 0;
listaCompleta = []
while x < 1:
    texto = input().split(' ')
    matricula = int(texto[0])
    mesAdmissao = int(texto[1])
    anoAdmissao = int(texto[2])
    mesSaida = int(texto[3])
    anoSaida = int(texto[4])

    if matricula == 0:
        break;
    else:
        listaInformacao = []
        tempoTotalAdmissao = (anoAdmissao * 12) + mesAdmissao
        tempoTotalSaida = (anoSaida * 12) + mesSaida
        tempoTotal = tempoTotalSaida - tempoTotalAdmissao
        listaInformacao.insert(0, matricula)
        listaInformacao.insert(1, tempoTotal)
        listaCompleta.insert(x, listaInformacao)

funcionarioPremiado = 0;
matriculaPremiado = 0;
while x < len(listaCompleta):
    dados = listaCompleta[x]
    if dados[1] > funcionarioPremiado:
        funcionarioPremiado = dados[1]
        matriculaPremiado = dados[0]
    x += 1
print(matriculaPremiado)