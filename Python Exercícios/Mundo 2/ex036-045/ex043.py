peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual sua altura (m) '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {str(imc).replace(".", ","):.4s}')

if imc < 18.5:
    print('Voce está em ABAIXO DO PESO!')
elif imc <= 25:
    print('Voce está em PESO NORMAL!')
elif imc <= 30:
    print('Voce está em SOBREPESO!')
elif imc <= 40:
    print('Voce está em OBESIDADE!')
else:
    print('Voce está em OBESIDADE MÓRBIDA!')
