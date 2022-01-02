# Fazer uma tupla com os 20 primeiros colcados do brasileirao de 2017 e mostra-los
tabela = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama',
               'Chapecoense', 'Atlético Mineiro', 'Botafogo', 'Atletico Paranaense', 'Bahia', 'São Paulo',
               'Fluminense', 'Sport', 'Vitoria', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atletico Goianiense')
print(20*'-=')
print('Lista de times do brasileirão: ', end='')
print(tabela)

# a) Mostrar os cinco primeiros elementos da tabela
print(20*'-=')
print(f'Os primeiros cinco são: {tabela[0:6]}')

# b) Os ultimos 4 colocados da tabela
print(20*'-=')
print(f'Os últimos 4 são: {tabela[-4:]}')

# c) Uma lista com todos os times em ordem alfabetica
print(20*'-=')
print(f'Times em ordem alfabetica: {sorted(tabela)}')

# d) Em que posiçao na tabela esta o time da chapecoense
print(20*'-=')
print(f'O chapencoense está na {tabela.index("Chapecoense")+1}ª posição')
