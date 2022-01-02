pergunta = ''
qntn, media, soma, maior, menor = 0, 0, 0, 0, 0
while pergunta != 'n':
    n = int(input('Digite um numero: '))
    pergunta = input('Quer contiruar [S/N]: ').lower()
    if qntn == 0:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    qntn += 1
    soma += n
    media = soma / qntn
print(f'Voce digitou {qntn} numero e a media entre eles foi de {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
