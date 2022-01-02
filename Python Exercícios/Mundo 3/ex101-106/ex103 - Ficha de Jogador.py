def ficha(nome='<desconhecido>', gols=0):
    """
    -> Imprime dados do jogador informado
    :param nome: Recebe o nome do Jogador
    :param gols: Recebe a quantidade de gols feitos por esse jogador
    """
    print(f'O Jogador {nome} fez {gols} gol(s) no campeonato')


print('_' * 30)
nome = input('Nome do Jogador: ').strip().capitalize()
gols = input('Quantos Gols: ').strip()
if gols.isnumeric():
    int(gols)
else:
    gols = 0 
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)
