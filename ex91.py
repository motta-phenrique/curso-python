from random import randrange
from operator import itemgetter

colocacao = list()

jogadores = {'jogador1': randrange(1,7),
             'jogador2': randrange(1, 7),
             'jogador3': randrange(1,7),
             'jogador4': randrange(1,7)
             }
for k, i in jogadores.items():
    print(f'{k} tirou {i}')

colocacao = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('-='* 40)

for j, itens in enumerate(colocacao):
    print(f'{j+1} lugar: {itens[0]} com {itens[1]}')
