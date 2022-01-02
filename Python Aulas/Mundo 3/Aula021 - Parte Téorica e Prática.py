# PARTE TEÓRICA DA AULA 021 SOBRE FUNÇÕES PARTE 2: EBA!!!!!!!!
# Nesta aula aprenderemos sobre:
#    1) Interactive Help
#    2) Docstrings
#    3) Argumentos opcionais
#    4) Escopo de variáveis
#    5) Retorno de resultados
# 
# 1) Vamos começar com Interactive Help:
#   Vamos usar o help() para saber sobre isso:
print('-=' * 30)
print('Vamos aprender utilizar o help():')
print('Para utilizarmos esse comando precisamos abrir o console do Python')
print('Ou posso fazer help(print)')
help(print)
print('-=' * 30)

print()

print('Posso fazer também print(input, __doc__): ')
print(input.__doc__)

print()

# 2) Vamos utilizar agora as docstrings que é exatamente o que acabamos de ver 
# vamos dar de exemplo uma situação:
#    def contador(i, f, p):
#        c = i
#        while c <= f:
#            print(f'{c}', end='')
#            c += p
#        print('FIM!')
#
# Eu sei exatamente como funciona essa função, mas
# quem não criou a função não sabe
# 

print('-=' * 30)
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Funcao criada por Rodrigo Barboni Filho do Brasil
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')


contador(0, 100, 10)
print('\nSe eu utilizar o help nessa função que nós criamos o que aparecerá?')

print()

help(contador)

print('-=' * 30)

print()

# 3) Parâmetros opcionais:
# Vamos criar a função somar():
#    def somar(a, b, c):
#        s = a + b + c
#        print(f'A soma vale {s}')
#
# Vamos dar de exemplo a situação que eu tenho uma função somar() que irá somar todos os números passados
# como parâmetro:
#    somar(3, 2, 5)  # Isto e parametro opcional e nao desempacotamento 
# Mas se eu chamar essa função com apenas dois parâmetros dará erro pois a variavel c não terá valor:
# Ou eu posso adicionar os parâmetros opcionais:
#    def somar(a=0, b=0, c=0):
#       s = a + b + c
#       print(f'A soma vale {s}')
# 
# E agora essa função sendo chamada com apenas dois parâmetros não dará mais erro:
#    somar(8, 4)
# Ela irá funcionar do mesmo jeito
print('Com parametros opcionais vamos criar a função somar():')
print('-=' * 30)
def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o PRIMEIRO valor
    :param b: o SEGUNDO valor
    :param c: o TERCEIRO valor
    :return: sem retorno
    Função criada por Rodrigo Barboni Filho do Brasil
    """
    s = a + b + c
    print(f'A soma vale {s}')

somar(b=4, c=2)
somar(3, 2, 5)
somar(1, 3)
somar(4)
somar()

# 4) Escopo de variaveis
# Para entendermos isso temos que fazer na pratica
# Programa Principal
print('-=' * 30)
print('Vamo criar um função chamada teste():')

# Entao temo aqui que x esta num escopo local e não podemos chama-lo pois está num escopo local
def teste():
    x = 9
    print(f'Na função teste, o n vale {n}.')
    print('Na função teste, x vale {x}')
print('Vamos fazer isso declarando uma variavel chamada "n" valendo 2:')

# E n está no escopo global:

n = 2
print(f'No programa principal. n vale {n}.')
teste()
print('No programa principal, vale x')
print()
print('Vamo fazer um teste com outra funçãoo:')
def teste1():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
print(f'N1 global vale {n1}')
teste1()
print()
print("""Se eu usar:
def teste(b):
    global a
    a = 8
    b += 4
    c = 2""")
print('Assim a variavel a que foi criada num escopo local passa a ser a que esta no escopo global')
print('-=' * 30)
print()

# 5) Vamos ver agora sobre a função return:
def somar(n1=0, n2=0, n3=0):
    s = n1 + n2 + n3
    return s


resp = somar(3, 2, 5) # OU
print(somar(3, 2, 5))

# PARTE PRATICA
def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= n
    return f


n1 = fatorial(5)
n2 = fatorial(4)
n3 = fatorial()
print(f'Os resultados são {n1}, {n2} {n3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par.')
else:
    print('Não é par.')
