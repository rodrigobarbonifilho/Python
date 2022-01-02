# VARIAVEIS SIMPLES
# variavel(lanche) = espaço
# para fazer uma atribuiçao utilizamos o sinaç '='
# e com esse sinal podemos colocar algo na variavel
# ex:
#   lanche = hamburguer
# hamburguer e alocado no espaço
# mas em outro momento queremos adicionar outra coisa nessa variavel
# ex:
#   lache = hamburguer
# e logo apos:
#   lanche = suco
# a variavel lanche vai substituir o hamburguer por suco por se tratar de uma variavel simples
#
# VARIAVEIS COMPOSTAS(onde se pode armazenar um item ou mais de um):
# * strings sao VARIAVEIS COMPOSTAS
# TUPLAS:
#   uma variavel que guarda varios valores
# COMO ACESSAR ELEMENTOS NA TUPLA:
#   a variavel(lanche) tem 4 elementos sendo eles:
#   hamburguer  suco   pizza   pudim
#       0        1       2       3      =  indices dos elementos
#
# Ex:
#   Se eu fizesse o comando:
#   print(lanche)
#
#   ele ira mostrar:
#   [hamburguer] [suco] [pizza] [pudim]
#
#   agora se eu fizer o comando:
#   print(lanche[2])
#
#   ele ira mostrar:
#   [pizza] - o item que esta na segunda indice
#
# FATIAMENTO DE TUPLAS:
# Podemos fatiar a tupla:
# Ex:
#   print(lanche[0:2])
#
#   Ele ira mostrar:
#   [hamburguer] [suco] - No fatiamento o Python ignora o ultimo elemento
#
# Outras formas de fatiar uma tupla:
# Ex:
#   print(lanche[1:])
#
#   Ira mostrar:
#   [suco] [pizza] [pudim] - ele começa no elemento de indice 1 e vai ate o final
#
#   print(lanche[-1])
#
# Ex:
#   Ira mostrar:
#   [pudim] - no caso o ultimo elemento 1}
#                                       }
#   [hamburguer] [suco] [pizza] [pudim] }
#        -4        -3     -2      -1
#
# Posso tambem utilizar a funçao len() na tupla:
# Referencia à length(comprimento) que diz quantos elementos tem a variavel composta lanche
# Ex:
#   len(lanche)
#
#   Ira mostrar:
#   4
#
# Tem como usar iteraçoes em tuplas:
# Ex:
#  O python cria uma variavel(c) no for (variavel simples)
#  for c in lanche:
#       print(c)
#
#  Ira mostrar:
#  [hamburguer]
#  [suco]
#  [pizza]
#  [pudim]
#
#  podemos usar o for com tuplas nao so com range()
#
#  --------------------------- METADE -------------------------------
#
# ATENÇÃO:
# AS TUPLAS SAO IMUTAVEIS!!!!
# Podemos mudar a tupla digitando o codigo, mas durante o programa nao
