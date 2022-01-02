# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date

# Pegando o ano atual
atual = date.today().year

# Declarando um dicionário
ficha = {
    'nome': '',
    'idade': 0,
    'ctps': 0
}

# Declarando os valores às keys dos dicionários
ficha['nome'] = input('Nome: ').strip().capitalize()
nasc = int(input('Ano de Nascimento: '))
ficha['idade'] = atual - nasc
ficha['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

# Declarando mais valores e keys ao dicionário dependendo do número do CTPS
if ficha['ctps'] != 0:
    ficha['contratação'] = int(input('Ano de Contratação: '))
    ficha['sálario'] = float(input('Salário: R$ '))
  # ficha['aposentadoria'] = ficha['idade'] + ((ficha['contratação'] + 35) - atual)
    ficha['aposentadoria'] = (ficha['contratação'] - nasc) + 35

# Mostrando os dados formatado
print('-=' * 30)
for k, v in ficha.items():
    print(f'  - {k} tem o valor {v}')
