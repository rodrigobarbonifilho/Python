from random import randint
from time import sleep

# Definindo as variaveis
palpites = [[]]
temp = []

# Enfeintando o programa
print('--' * 17)
print(f'{"JOGOS NA MEGA SENA":^34}')
print('--' * 17)

qnt_de_palpites = int(input('Quantos jogos você quer que eu sorteie: '))

print(f'-=-=-=-= Sorteando {qnt_de_palpites} jogos -=-=-=-=')

# Colocando os números dentro da lista
for l in range(1, qnt_de_palpites+1):
    for n in range(0, 6):
        num = randint(0, 60)
        temp.append(num)
    
    for i, n in enumerate(temp):
        if temp.count(n) == 2:
            temp.remove(n)
            temp.insert(i, randint(0, 60))
            break
    
    palpites.sort()
    palpites.append(temp[:])
    temp.clear()
    print(f'{l}° Jogo: {palpites[l]}')
    sleep(1)

print(palpites)

print('-=-=-=-=-= < Boa Sorte > -=-=-=-=-=')


# Jeito Guanabara
from random import randint
lista = list()
jogos = list()
print('-' * 30)
print(f'{"Jogo na mega sena":^30}')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1 
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f' Jogo {i+1}°: {l}')
    sleep(1)
print('-=' * 5, ' < BOA SORTE > ', '-=' * 5)
