# coding=utf-8
"""salario = float(input('Coloque aqui o valor do salario do funcionario:R$'))
aumento = salario * 15 / 100
aumento2 = aumento + salario
print('O funcionario que ganhava R${},agora com o aumento de 15%,ganhará R${}'.format(salario, aumento2))"""

# Tenta de outro jeito

nome = input('Coloque aqui o nome do funcionario:')
salario = float(input('Coloque aqui o valor do salario do {}:R$'.format(nome)))

aumento0 = int(input('Coloque aqui a porcentage do aumento:%'))
aumento1 = salario * aumento0 / 100
aumento2 = salario + aumento1

print()

print('\033[1;31mO funcionario {} que ganhava R${:.2f},'
      'agora com o aumento de {}% ganhará R${:>2f}\033[m'.format(nome, salario, aumento0, aumento2))
