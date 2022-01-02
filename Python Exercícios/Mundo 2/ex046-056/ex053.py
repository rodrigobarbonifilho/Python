# Versao sem for
frase = input('Digite uma frase: ').replace(' ', '').upper()
inverso = frase[::-1]
print(f'O inverso de {frase} é {inverso}')
if inverso == frase:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palindromo!')

print()

# Versao com for
frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
invertido = ''
for l in range(len(junto) - 1, -1, -1):
    invertido += junto[l]
print(f'O inverso de {junto} é {invertido}')
if junto == invertido:
    print('Temos um palindromo!')
else:
    print('A frase digitada nao e um palindromo!')
