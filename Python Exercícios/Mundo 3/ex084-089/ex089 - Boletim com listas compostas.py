from time import sleep

# Criar um programa que leia o nome e nota de uma aluno e depois mostre de forma tabular

# Variaveis
alunos = list()
temp = list()
media = 0

# Ler o nome
while True:
    print('-=' * 3, 'Cadastro do aluno', '-=' * 3)    
    aluno = input('Nome do aluno: ').strip().capitalize()

# Ler as 2 notas
    nota1 = float(input('Nota 1: '))
    while nota1 > 10:
        print('Não é possivel uma nota maior que 10. Tente Novamente:')
        nota1 = float(input('Nota 1: '))
    
    nota2 = float(input('Nota 2: '))
    while nota2 > 10:
        print('Não é possivel uma nota maior que 10. Tente Novamente:')
        nota2 = float(input('Nota 2: '))

# Adicionando a lista temp e jogando na lista alunos
    media = (nota1 + nota2) / 2
    temp.append(aluno)
    temp.append(nota1)
    temp.append(nota2)
    temp.append(media)
    alunos.append(temp[:])
    temp.clear()

# Confirmando a resposta
    print('-=' * 5, 'Resposta', '-=' * 5)
    resp = input('Quer continuar? [S/N]: ')[0]
    while resp not in 'SsNn':
        resp = input('Tente Novamente. Quer continuar? [S/N]: ')[0]
    if resp in 'Nn':
        break

print('-=' * 30)
# Mostrar os dados de forma tabular
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":<8}')
print('--' * 12)
for i, l in enumerate(alunos):
    print(f'{i:<4}{l[0]:<10}{l[3]:^8.1f}')

# Fazer uma função para ver as notas de um aluno específico
print('--' * 12)
while True:
    nota_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if nota_aluno == 999:
        break
    if nota_aluno <= len(alunos)-1:
        print(f'Notas de {alunos[nota_aluno][0]} são: [{alunos[nota_aluno][1]}, {alunos[nota_aluno][2]}]')
        print('--' * 12)
    else:
        print('Aluno não existente no cadastro!')
print('FINALIZANDO...')
sleep(1)
print('<<< VOLTE SEMPRE >>>')
