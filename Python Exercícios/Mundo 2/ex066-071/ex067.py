cont = 0
print(40*'-')
while True:
    n = input('Quer ver a tabuada de qual valor? ')
    print(40*'-')
    if '-' in n:
        break
    while cont < 10:
        cont += 1
        print(f'{n} x {cont} = {int(n)*int(cont)}')
        if cont == 10:
            cont = 0
            print(40*'-')
            break
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')
