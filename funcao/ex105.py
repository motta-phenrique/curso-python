def notas(*num, s= False):
    boletim = dict()
    maior = 0
    menor = 11
    media = 0
    boletim['quantidade'] = len(num)

    for i in num:
        if i > maior:
            maior = i

        if i < menor:
            menor = i

        media += i

    media = media / len(num)

    boletim['maior'] = maior
    boletim['menor'] = menor
    boletim['media'] = media

    if s:

        if media > 8:
            boletim['situacao'] = 'Otima'
        elif media >= 7:
            boletim['situacao'] = 'Boa'
        elif media < 7:
            boletim['situacao'] = 'Ruim'

    return boletim

reposta = notas(9.8, 9.4, 9,)
print(reposta)

