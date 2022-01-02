# coding=utf-8
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\
# Iteraçao While(Estrtura de controle com consiçao logica)
# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# O While diferente do for serve para uma iteraçao que se sabe o limite ou não

"""for c in range(1, 10):
    print(c)
print('FIM')
print()

c = 1
while c < 10:
    print(c)
    c += 1 # ou c = c + 1
print('FIM')

for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('FIM')

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = input('Quer continuar? [S/N] ').upper()"""

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Voce informou {} numeros pares e {} numeros impares'.format(par, impar))
