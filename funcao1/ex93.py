jogador = dict()
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

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')

for i, pos in enumerate(jogador['aproveitamento']):
    print(f'---------> Na partida {i+1} marcou {jogador["aproveitamento"][i]} gols')

print(f'No total marcou {jogador["total_gols"]} gols')
