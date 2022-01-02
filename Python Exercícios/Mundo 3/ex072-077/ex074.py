from random import randint as ri
# Gerar variaveis com numeros aleatorios
a, b, c, d, e = ri(1, 10), ri(1, 10), ri(1, 10), ri(1, 10), ri(1, 10)

# Colocar essas variaveis dentro de uma tupla
numerosAleat = (a, b, c, d, e)

# Ver qual numero sorteado e o maior
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
if d > maior:
    maior = d
if e > maior:
    maior = e

# Ver qual numero sorteado e o menor
menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c
if d < menor:
    menor = d
if e < menor:
    menor = e

# Mostrar os numero sorteados
print('Os numeros sorteados foram: ', end=' ')
for n in numerosAleat:
    print(n, end=' ')

# Mostrar qual foi o maior e qual o menor
print(f'\nO maior numero foi: {maior}')
print(f'O menor numero foi: {menor}')
