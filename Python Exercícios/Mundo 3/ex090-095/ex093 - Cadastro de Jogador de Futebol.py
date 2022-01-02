ficha = {
    'nome': '',
    'gols': [],
    'total': 0
}
tot = 0

ficha['nome'] = input('Nome do Jogador: ')
quantidade_de_partidas = int(input(f'Quantas partidas {ficha["nome"]} jogou: '))

for c in range(0, quantidade_de_partidas):
    gols = int(input(f' => Quantos gols na partida {c}: '))
    ficha['gols'].append(gols)
    tot += gols
ficha['total'] = tot

print('-=' * 30)
print(ficha)
print('-=' * 30)
for k, v in ficha.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {ficha["nome"]}, jogou {quantidade_de_partidas} partidas.')
for i, n in enumerate(ficha['gols']):
    print(f'    => Na partida {i}, fez {n} gols.')
print(f'Foi um total de {ficha["total"]} gols.')
