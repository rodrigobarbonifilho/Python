from random import randint

from time import sleep

computador = randint(1,5) # Faz o computador "PENSAR"

print(20 * '-=-')
print('Vou pensar num numero de 0 a 5,tente adivinha-lo...')
print(20 * '-=-')

jogador = int(input('Qual numero eu pensei? ')) # Aqui o jogador chuta um numero

print('PROCESSANDO...')
sleep(2)

if jogador == computador:
    print('\033[1;32mPAARABENS! Voce conseguiu me vencer!\033[m')
else:
    print('\033[1;31mPERDEU! Eu pensei no numero {} e nao no {}!\033[m'.format(computador, jogador))
