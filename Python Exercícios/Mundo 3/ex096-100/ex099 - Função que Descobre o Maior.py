from time import sleep


def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    
    sleep(1)
    
    for n in num:
        print(n, end=' ', flush=True)
        sleep(0.5)
    print(f'Foram passados ao todo {len(num)} valores')
    
    cont = 0
    if len(num) != 0:
        for n in num:
            if cont == 0:
                maiorn = n
            elif n > maiorn:
                maiorn = n
            cont += 1
        print(f'O maior valor informado foi {maiorn}')
    else:
        print('O maior valor informado foi 0')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 7, 3)
maior(1, 2)
maior(6)
maior()
