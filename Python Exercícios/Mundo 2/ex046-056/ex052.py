num = int(input('Digite um numero: '))
if num > 0:
    divisores = 0
    for n in range(1, num+1):
        cont_divisores = num % n
        if cont_divisores == 0:
            divisores += 1
        else:
            divisores += 0
        if num % n == 0:
            cor = '\033[1;33m'
            fim = '\033[m'
        else:
            cor = '\033[1;31m'
            fim = '\033[m'
        print(f'{cor}{n}{fim}', end=' ')
    print(f'\nO numero {num} foi divisivel {divisores} vezes')
    if divisores == 2:
        print('E por isso este número é PRIMO!')
    elif divisores >= 3:
        print('E por isso este número não É PRIMO!')
    else:
        print('1 não é PRIMO!')
else:
    print('0 não é válido!')
