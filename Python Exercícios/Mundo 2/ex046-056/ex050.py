s, c = 0, 0
for n in range(1, 7):
    num = int(input(f'Digite aqui o {n}° numero inteiro: '))
    if num % 2 == 0:
        s += num
        c += 1
print()
print(f'Voce informou {c} numero(s) PAR(ES), e a soma é igual: {s}')
