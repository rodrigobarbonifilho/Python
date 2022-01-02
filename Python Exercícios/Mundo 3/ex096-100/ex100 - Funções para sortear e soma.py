# Bibliotecas
from random import randint
from time import sleep

# Variaveis compostas
numeros = list() 

# Funções
def sorteia(lista):
    numeros.clear()
    cont = 0
    while cont <= 5:
        lista.append(randint(1, 10))
        cont += 1
        if cont == 5:
            break


def somaPar(lista):
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    print(s)


# Programa principal
print('Sorteando 5 valores: ', end='')
sorteia(numeros)
for n in numeros:
    print(n, end=' ', flush=True)
    sleep(0.5)
print('PRONTO!')
print(f'Somando os valores pares de {numeros}, Temos ', end='')
somaPar(numeros)
# Fim
