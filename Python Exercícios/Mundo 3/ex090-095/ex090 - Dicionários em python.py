aluno = {}

aluno['nome'] = input('Nome: ').strip().capitalize()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

while aluno['media'] > 10:
    aluno['media'] = float(input('ERRO! Não aceitamos nota maior que 10: '))

print('-=' * 30)

if aluno['media'] <= 3:
    aluno['situação'] = 'Reprovado'
elif 7 > aluno['media'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'

for k, v in aluno.items():
    print(f'    - {k} é igual a: {v}')
