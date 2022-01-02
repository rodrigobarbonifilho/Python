n, soma, qntn = 0, 0, 0
while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    if n != 999:
        soma += n
        qntn += 1
print(f'Voce digitou {qntn} numeros e a soma entre eles foi {soma}.')
