n = int(input('''Digite aqui um numero
Para ver seu fatorial: '''))
f = n
print(f'Calculando {n}! = ', end='')
while n != 1:
    print(f'{n}', end='')
    if n == 2:
        print(' x 1 = ', end='')
    else:
        print(' x ', end='')
    n -= 1
    f *= n
print(f)
