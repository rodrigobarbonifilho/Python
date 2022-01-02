# Definindo variaveis para solicitar o emprestimo
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
ano = int(input('Quanto anos de financiamento? '))

# Definindo variaveis para o emprestimo ser solicitado ou nao
emprestimo = (casa / (ano * 12))
limite = salario * 30 / 100

# Se o emprestimo vai ser aprovado
print('\033[1;33mPara pagar uma casa de R${:.2f} em {} anos'.format(casa, ano), end=' ')
print('a prestaçao sera de R${:.2f}'.format(emprestimo))


if emprestimo <= limite:
    print('\033[1;32mEmprestimo pode ser CONCEDIDO!\033[m')
elif emprestimo > limite:
    print('\033[1;31mEmprestimo NEGADO!\033[m')
else:
    print('--ErRor--')
