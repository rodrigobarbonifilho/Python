# coding=utf-8
from time import sleep
from random import randint

cpu = randint(1, 3)
pd = 'PEDRA'
pp = 'PAPEL'
t = 'TESOURA'

print('''\033[1;mSuas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogador = input('Qual a sua jogada? ')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

# Vendo qual a escolha do jogador
if jogador == '1':
    jogador = pd
elif jogador == '2':
    jogador = pp
elif jogador == '3':
    jogador = t
else:
    jogador, cpu = 'Nada', 'Nada'

# Vendo qual a escolha do computador
if cpu == 1:
    cpu = pd
elif cpu == 2:
    cpu = pp
elif cpu == 3:
    cpu = t

print(11*'\033[34m-=\033[m')
print(f'\033[1;34mComputador jogou {cpu}\033[m')
print(f'\033[1;34mJogador jogou {jogador}\033[m')
print(11*'\033[34m-=\033[m')

if jogador == pd and cpu == t or jogador == pp and cpu == pd or jogador == t and cpu == pp:
    print('\033[1;32mJogador GANHOU!\033[m')
elif jogador == cpu:
    if jogador and cpu == 'Nada':
        print('\033[1;31mTentou bugar né!\033[m')
    else:
        print('\033[1;33mEMPATE!\033[m')
elif cpu == pd and jogador == t or cpu == pp and cpu == pd or cpu == t and jogador == pp:
    print('\033[1;31mCpu Ganhou!\033[m')
