# coding=utf-8
nome = input('\033[1;34mQual o nome do funcionario(a)? \033[m')
salario = float(input('Qual o valor do salario do funcionario(a) {}: '.format(nome)))
aumento = salario * 15 / 100 + salario
porcentagem = 15
if salario >= 1250:
    porcentagem = 10
    aumento = salario * 10 / 100 + salario
print('O funcionario(a) {},que ganhava R${:.2f},'
      'agora com o aumento de {}%,ganhará R${:.2f}'.format(nome, salario, porcentagem, aumento))
