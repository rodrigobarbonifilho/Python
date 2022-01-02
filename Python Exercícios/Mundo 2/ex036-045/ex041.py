from datetime import date

ano_atual = date.today().year
ano_de_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_de_nascimento
print(f'O Atleta tem {idade} anos.')

# Vendo qual a classifição
classificacao = 'Classe nao identificada!'
if idade <= 9:
    classificacao = 'Mirim'
elif idade <= 14:
    classificacao = 'Infantil'
elif idade <= 19:
    classificacao = 'Júnior'
elif idade <= 25:
    classificacao = 'Sênior'
elif idade > 25:
    classificacao = 'Master'
print(f'Classificação: {classificacao}')
