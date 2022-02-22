from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'jogador1': randint(1, 20),
    'jogador2': randint(1, 20),
    'jogador3': randint(1, 20),
    'jogador4': randint(1, 20)
}
ranking = dict()
print('Valores sorteados')
for player, value in jogo.items():
    print(f'{player} - Dado:{value}')
    sleep(0.7)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-'*30)
for i,v in enumerate(ranking):
    print(f'{i+1}º Lugar:{v[0]} com {v[1]}')
    sleep(0.4)