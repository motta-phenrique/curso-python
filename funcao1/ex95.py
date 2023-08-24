jogador = dict()
elenco = list()

while True:
    total_gols = 0
    jogador['nome'] = input('Digite o nome do jogador: ')
    jogador['partidas'] = int(input('Digite a quantidade de partidas: '))

    gols_part = list()

    for i in range(0, jogador['partidas']):
        gols = int(input(f'gols na partida {i + 1}: '))
        total_gols += gols
        gols_part.append(gols)

    print('+=' * 30)

    jogador['aproveitamento'] = gols_part[:]
    jogador['total_gols'] = total_gols

    elenco.append(jogador.copy())

    escolha = input('Digite continuar: [S][N] ').upper()

    if escolha == 'N':
        break


print("Nome --- partida - gols por partida --- total de gols")

for jog in elenco:
    for i in jog.values():
        print(f'{i}')
    print()

