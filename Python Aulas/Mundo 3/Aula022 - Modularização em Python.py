# Parte Teórica da Aula 022 sobre Mudularização:
# 
# Explicação:
# O que é Modularização e Pacotes:
# Modularização é a arte de fazer módulos:
#   . Surgiu no ínicio da década de 60
#   . Sistemas ficando cada vez maiores
#   . Foco: Dividir um programa grande
#   . Foco: Aumentar a legibilidade
#   . Foco: Facilitar a manutenção
# 
# Vamos imaginar a seguinte situação:
#
#    def fatorial(n):
#        f = 1
#        for c in range(1, n+1):
#            f *= c
#        return f
#
#    num - int(input('Digite um valor'))
#    fat = fatorial(num)
#    print(f'O fatorial de {num} é {fat}')
# 
# Que é o mesmo de:
#    from úteis import fatorial
#    from math import sqrt
#    from datetime import datetime
#    from random import randint
# 
# Vantagens:
#    . Organização do Código
#    . Facilidade na manuntenção 
#    . Ocultação de código detalhado
#    . Reutilização em outros projetos
# 
# E também podemos usar os Pacotes ou Bibliotecas:
print('Parte Prática: ')
print('O Pacote nada mais é do que uma pasta cheia de módulos. E para usá-los é só importar ele usando: ')
print('import úteis # Que é o pacote.')
print('E para criarmos um é só criar uma pasta com pastas separadas: ')
print('Precisamos do arquivo __init__.py dentro desse pacote')
