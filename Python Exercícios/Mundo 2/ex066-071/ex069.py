pm18, hc, mm20 = 0, 0, 0
while True:
    print(30*'\033[1;m-')
    print(f'{" CADASTRE UMA PESSOA ": ^30}')
    print(30*'\033[1;m-\033[m')
    idade = int(input('Idade: '))
    if idade > 18:
        pm18 += 1
    sexo = input('Sexo [M/F]: ').upper().strip()[0]
    if sexo == 'M':
        hc += 1
    if idade < 20 and sexo == 'F':
        mm20 += 1
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo [M/F]: ').upper().strip()[0]
    print(30*'\033[1;m-\033[m')
    resposta = input('Voce quer continuar? [S/N]: ').upper().strip()[0]
    while resposta not in 'SN':
        resposta = input('Voce quer continuar? [S/N]: ').upper().strip()[0]
    if resposta == 'N':
        break
print(30*'\033[1;m-\033[m')
print(f'''No total {pm18} pessoas tem mais de 18 anos.
Ao todo temos {hc} homem(ns) cadastrado(s).
E temos {mm20} mulher(s) com menos de 20 anos.''')
