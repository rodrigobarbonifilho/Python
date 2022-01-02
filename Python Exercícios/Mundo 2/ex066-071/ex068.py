from random import randint
cpu = randint(1, 10)
pv = 0
print(20*'-=')
print('VAMOS JOGAR PAR OU IMPAR!')
print(20*'-=')
while True:

    # A opçao do jogador
    valor = int(input('Diga um valor: '))
    jogador = input('Par ou Impar [P/I]: ').upper().strip()[0]
    soma = valor + cpu

    # Vendo se a soma dos valores foi IMPAR ou PAR
    if soma % 2 == 1:
        resultado = 'IMPAR'
    else:
        resultado = 'PAR'

    # Mostrando para o usuario se a soma foi IMPAR ou PAR
    print(20*'--')
    print(f'Voce jogou {valor} e computador {cpu}. Total de {soma} DEU {resultado}')
    print(20*'--')

    # Mostrando se o usuario VENCEU ou PERDEU
    if jogador == 'P' and resultado == 'PAR' or jogador == 'I' and resultado == 'IMPAR':
        print('\033[1;32mVoce VENCEU!')
        print('Vamos jogar novamente...\033[m')
        pv += 1
    elif jogador == 'P' and resultado == 'IMPAR' or jogador == 'I' and resultado == 'PAR':
        break
    else:
        print("Voce nao informou se queria 'IMPAR' ou 'PAR', entao voce nao ganhou nem perdeu!")
    print(20*'-=')

# Mostrando o final do programa
if pv == 0:
    print('\33[1;31mGAME OVER! Voce nao ganhou nenhuma vez!')
else:
    print(f'\33[1;31mGAME OVER! Voce venceu {pv} vez(es).\33[m')
