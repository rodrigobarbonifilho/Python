# Variaveis compostas

ficha = {}
lista = []

# Inicio

while True:
    print('-=' * 30)

    ficha['nome'] = input('Nome: ').strip().capitalize()
    
    ficha['gols'] = []
    
    partidas = int(input(f'Quantas partidas {ficha["nome"]} jogou? '))

    for c in range(1, partidas+1):
        ficha['gols'].append(int(input(f'Quantos gols na partida {c}: ')))
    resp = input('Quer continuar? [S/N]: ').upper()[0]
    
    while resp not in 'SN':
        print('ERRO! Somente digite S ou N!')
        resp = input('Quer continuar? [S/N]: ').upper()[0]
    ficha['total'] = sum(ficha['gols'])
    lista.append([ficha.copy()])
        
    if resp == 'N':
        break

print('-=' * 30)

print(f'{"cod":3} {"nome":<10}{"gols":^20}{"total":>14}')

print('--' * 26)
for i, l in enumerate(lista):
    for d in l:
        print(f'{i:>3} {d["nome"]:<18}{str(d["gols"]):<15}{d["total"]:>8}')
print('--' * 26)

while True:
    esc = int(input('Mostrar dados de qual jogo? (999 para interromper): '))

    if esc == 999:
        break

    while esc >= len(lista):
        print('-=' * 30)
        print(f'ERRO! Não temos nenhum jogador de cod {esc} no cadastro.')
        esc = int(input('Mostrar dados de qual jogo? (999 para interromper): '))
    
    print('-=' * 30)
    
    print(f'-- LEVANTAMENTO DO JOGADOR {lista[esc][0]["nome"]}:')

    for i, l in enumerate(lista[esc][0]['gols']):
        print(f'  No jogo {i}: fez {l} gols')

# Fim
print('-=' * 30)
print('<< VOLTE SEMPRE >>')