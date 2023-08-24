def jogador(n = "", g = ''):
    if n == "":
        n = '<desc>'

    if g == '':
        g = '0'

    return f'o jogador {n} marcou {g} gol(s)'


nome = input('Digite o nome: ')
gols = input('Total de gols: ')

print(jogador(nome, gols))
