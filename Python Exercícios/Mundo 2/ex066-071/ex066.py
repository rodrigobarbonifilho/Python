n = soma = qntn = 0
while True:
    n = int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    soma += n
    qntn += 1
print(f'A soma entre os {qntn} valores informados é de {soma}!')
