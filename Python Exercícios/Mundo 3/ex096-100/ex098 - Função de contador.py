from time import sleep

def contador1():
    print('-=' * 30)
    print('Contagem de 1 até 10 de 1 em 1:')
    for n in range(1, 11):
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('FIM!!')
    print('-=' * 30)
    print('Contagem de 10 até de 2 em 2:')
    for n in range(10, -2, -2):
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('FIM!!')
    print('-=' * 30)
    print('Agora é a sua vez de personalizar a sua contagem!!')
    inicio = int(input('Inicio: '))
    fim = int(input('Fim:    '))
    passo = int(input('passo:  '))

    if passo == 0:
        passo = 1

    print('-=' * 30)
    print(f'Sua contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    
    if inicio > fim:
        fim -= 1
        if passo > 0:
            passo *= -1
    else:
        fim += 1

    for n in range(inicio, fim, passo):
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('FIM!!')


# contador1()


def contador2(inicio, fim, passo):
    if passo == 0:
        passo = 1
    
    if inicio > fim:
        fim -= 1
        if passo > 0:
            passo *= -1
    else:
        fim += 1

    for n in range(inicio, fim, passo):
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('FIM!!')

print('-=' * 30)
print('Contagem de 1 até 10 de 1 em 1:')
contador2(1, 10, 1)
print('-=' * 30)
print('Contagem de 10 até 0 de 2 em 2:')
contador2(10, 0, 2)
print('-=' * 30)
print('Agora personalize a sua contagem!!')
i = int(input('Inicio: '))
f = int(input('Fim:  '))
p = int(input('Passo: '))
print('-=' * 30)
print(f'Contagem de {i} até {f} de {p} em {p}.')
contador2(i, f, p)