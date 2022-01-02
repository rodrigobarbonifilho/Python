from random import randint
from time import sleep
from operator import itemgetter
# Meu Jeito
print('-=' * 40)
print('Valores sorteados:')
jogadores = {}
for c in range(1, 5):
    num = randint(1, 6)
    print(f'jogador{c} tirou {num} no dado.')
    sleep(1)
    jogadores[f'jogador{c}'] = num
print('-=' * 40)
print(f'   == RANKING DOS JOGADORES ==')

for c in range(1, 5):
    print(f'    {c}° Lugar: jogador{c} com {jogadores[f"jogador{c}"]}')
    sleep(1)

print('-=' * 40)

# Jeito Guanabara
jogos = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

ranking = list()

print('Valores sorteados:')

for k, v in jogos.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-=' * 40)

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'  {i+1}° Lugar: {v[0]} com {v[1]}.')
    sleep(1)
