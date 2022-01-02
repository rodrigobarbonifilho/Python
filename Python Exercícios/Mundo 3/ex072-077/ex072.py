numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'trezes', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um numero entre 0 e 20: '))
while n > 20 or n < 0:
    n = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
print(f'Voce digitou o numero {numeros[n]}')
