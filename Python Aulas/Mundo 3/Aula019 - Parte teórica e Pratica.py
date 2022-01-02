# Aula 19 De Dicionarios
# Parte Teórica
# Estruturas compostas:
#   . São estruturas de dados que se pode colocar mais de uma coisa nela
# 
# Como vimos nas outras aulas:
#   .      Tuplas = ()
#   .      Listas = []
#   . Dicionários = {}
# 
# Vamos supor que temos a lista:
#    dados = [['Pedro', 25]]
# Podemos usar um dicionário:
#    dados = dict{}
#    dados = {'nome':'Pedro',
#             'idade': 25}
# E podemos usar a key(chave de índice) para usarmos o print:
#    print(dados['nome']) -> Pedro
#    print(dados['idade']) -> 25
# 
# E para adicionarmos algo a um dicionário não podemos usar o append() e sim:
#    dados['sexo'] = 'M'
# E simplesmente ele criará este elemento e para removermos algum elemento usamos o del:
#    del(dados['sexo'])
# 
# Se usarmos um dicionário para filmes:
#    filme = {'titulo': 'Star Wars',
#             'ano': 1997
#             'diretor': 'George Lucas'
#            }
# 
# Se eu usar o print(filme.values()):
#    Ira retornar os valores:
#        {'Star Wars', 1977, 'George Lucas'}
# Se usarmos o print(filme.keys()):
#    Ira mostrar todas as chaves:
#        {'titulo', 'ano', 'diretor'}
# Se usarmos o print(filme.items()):
#    Ira mostrar o dicionário: 
#        {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
# 
# Podemos usar os comandos acima num for:
#    for k, v in filme.items():
#        print(f'O {k} é {v})
# 
# Saída:
#    O título é Star Wars
#    O ano é 1977
#    O diretor é George Lucas
# 
# Posso juntar também uma lista dentro de uma tupla e etc:
#    Ex:
#        locadora = []
#        locadora.append(filmes)
# Que irá adicionar esse dicionário a lista locadora
# 
# ////////////////////////////////////// PARTE PRATICA \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Vamos criar um dicionário:
print('Vamos criar um dicionário pessoas.')
pessoas = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 22
}

# Se eu der pessoas[0] dará erro
# Então usamos a key 'nome' assim:
print('Se eu der pessoas[0] dará erro então usamos a key "nome" assim: ')
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])

print()

# Posso fazer também:
print('Posso fazer também:')
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos!')

print()

# Posso mandar ele imprimir só as chaves:
print('Posso mandar ele imprimir só as chaves:')
print(pessoas.keys())

print()

# Posso fazer de forma similar com o valores:
print('Posso fazer de forma similar com o valores:')
print(pessoas.values())

print()

# De forma similar posso mostrar os itens também:
print('De forma similar posso mostrar os itens também:')
print(pessoas.items())

print()

# Posso acessar também os valores e keys por laços:
print('Posso acessar também os valores e keys por laços:')
for k, v in pessoas.items():
    print(f'{k} = {v}')

print()

# Posso atribuir a uma key outro valor:
print('Posso atribuir a uma key outro valor:')
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')

print()
pessoas['nome'] = 'Gustavo'

# Posso adicionar itens somente declarando eles ex:
print('Posso adicionar itens somente declarando eles ex:')
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')

print()

# Podemos apagar o sexo usando o del:
print('Podemos apagar o sexo usando o del:')
del(pessoas['sexo'])
for k, v in pessoas.items():
    print(f'{k} = {v}')

print()

# Posso criar um dicionário dentro de uma lista:
print('Posso criar um dicionário dentro de uma lista:')
brasil = []
estado1 = {
    'uf': 'Rio de Janeiro',
    'sigla': 'RJ'
}
estado2 = {
    'uf': 'São Paulo',
    'sigla': 'SP'
}
brasil.append(estado1)
brasil.append(estado2)

# Se em mandar printar estado1:
print('Se em mandar printar estado1: ', end='')
print(estado1)

# Se eu mandar printar estado2:
print('Se eu mandar printar estado2: ', end='')
print(estado2)

# E se eu mandar printar brasil:
print('E se eu mandar printar brasil: ', end='')
print(brasil)

print()

# Pegando itens da lista e dicionarios:
print('Pegando itens da lista e dicionarios:')

print()

# Posso mandar printar brasil[0]:
print('Posso mandar printar brasil[0]: ', end='')
print(brasil[0])

# Ou brasil[1]:
print('Ou brasil[1]:', end='')
print(brasil[1])

print()

# E se eu mandar printar brasil[0]["uf"]:
print('E se eu mandar printar brasil[0]["uf"]: ', end='')
print(brasil[0]['uf'])

# Ou brasil[1]["sigla"]:
print('Ou brasil[1]["sigla"]: ', end='')
print(brasil[1]['sigla'])

print()

# Vamos fazer um exemplo que vai dar um errinho:
print('Vamos fazer um exemplo que vai dar um errinho:')
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = input('Unidade federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado)
print(brasil)

print()

# Para consertar este erro usamos o metodo .copy():
print('Para consertar este erro usamos o metodo .copy():')
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = input('Unidade federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(f'{v} ', end='')
    print()
