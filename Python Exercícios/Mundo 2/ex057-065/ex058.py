from random import randint as r
cpu = int(r(0, 10))
tentativas = 1
print('Eu sou seu computador...')
print('Acabei de pensar num numero de 0 a 10.')
print('Será que você consegue adivinhar qual foi?')
palpite = int(input('Qual é o seu palpite? '))
while palpite != cpu:
    if palpite != cpu and palpite > cpu:
        print('Menos...Tente mais uma vez!')
        palpite = int(input('Qual é o seu palpite? '))
        tentativas += 1
    elif palpite != cpu and palpite < cpu:
        print('Mais...Tente mais uma vez!')
        palpite = int(input('Qual é o seu palpite? '))
        tentativas += 1
if palpite == cpu and tentativas == 1:
    print('Prabens! Voce acertou de primeira!')
elif palpite == cpu:
    print(f'Depois de {tentativas} tentativas, voce acertou')
