# PARTE TEÓRICA SOBRE:
#    FUNÇÕES - PARTE 1
# Que coisas nós fazemos constantemente:
#    algumas delas são:
#        print()
#        len()
#        input()
#        int()
#        float()
#    Entre outras
# Essas funções são build-ins
# 
# E podemos usar essas funções para coisas que fazemos rotineiramente,
# como por exemplo se quisermos podemos criar uma função para mostrar linhas:
#    mostraLinha()
# Que por exemplo a saída seria:
#  -----------------------------------------------------------
# 
# Assim criaremos uma função para poder facilitar a nossa produção.
# Usamos isso para rotinas. 
# 
# Um exemplo seria:
#    print('------------------------------------')
#    print('         SISTEMA DE ALUNOS          ')
#    print('------------------------------------')
#    print('------------------------------------')
#    print('      CADASTRO DE FUNCIONÁRIOS      ')
#    print('------------------------------------')
#    print('------------------------------------')
#    print('          ERRO DO SISTEMA!          ')
#    print('------------------------------------')
# Podemos perceber que temos 6 print() literalmente iguais.
# Quer virou uma rotina.
# Podemos definir uma função assim:
#
#    def mostraLinha():
#        print('------------------------------------')
# 
# E com isso podemos reescrever aquele código acima: 
#    mostraLinha()
#    print('         SISTEMA DE ALUNOS          ')
#    mostraLinha()
#    mostraLinha()
#    print('      CADASTRO DE FUNCIONÁRIOS      ')
#    mostraLinha()
#    mostraLinha()
#    print('          ERRO DO SISTEMA!          ')
#    mostraLinha()
# 
# E o resultado será o mesmo
# PARTE PRATICA DA TEÓRICA SOBRE FUNÇÕES:
print()

print('Vamos fazer um exemplo sem as funções primeiro:')
print('-' * 30)
print(f'{"CURSO EM VIDEO":^30}')
print('-' * 30)
print('-' * 30)
print(f'{"APRENDA PYTHON":^30}')
print('-' * 30)
print('-' * 30)
print(f'{"GUSTAVO GUANABARA":^30}')
print('-' * 30)

print()

print('Vamos criar uma função agora e o resultado será o mesmo: ')
def lin():
    print('-' * 30)
lin()
print(f'{"CURSO EM VIDEO":^30}')
lin()
lin()
print(f'{"APRENDA PYTHON":^30}')
lin()
lin()
print(f'{"GUSTAVO GUANABARA":^30}')
lin()

# VOLTANDO PARA A PARTE TEÓRICA DA PARTE TEÓRICA '0':
# Posso criar uma função com parâmetros assim:
#    def mensagem(msg):
#        print('-' * 30)
#        print(f'{msg:^30}')
#        print('-' * 30)
# Então se chamarmos essa função:
# mensagem('SISTEMA DE ALUNOS')
# A saída será:
#    print('------------------------------------')
#    print('         SISTEMA DE ALUNOS          ')
#    print('------------------------------------')
# VOLTANDO DA PARTE TEÓRICA QUE TINHA IDO PRA PARTE PRATICA E QUE ESTA VOLTANDO:
print()

print('Criando uma função para títulos: ')
def titulo(text):
    print('-' * 30)
    print(f'{text:^30}')
    print('-' * 30)


# Programa principal
titulo('CURSO EM VIDEO')
titulo('APRENDA PYTHON')
titulo('GUSTAVO GUANABARA')
titulo('PYTHON É MUITO BOM')
titulo('OI')

print()

# PARTE PRATICA
print('Quando temos coisas repetitivas no programa podemos fazer um função para aquela rotina')

a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

print()

print('Assim:')

def soma(a, b):
    print(f'a = {a} e b = {b}')
    s = a + b
    print(s)
    print()


soma(4, 5)
soma(8, 9)
soma(2, 1)      # Estes numeros dentro dos paranteses são chamados de parâmetros
soma(b=3, a=2)  # Fazendo uma inversão de parametros
soma(a=3, b=2)  # E como na função recebe dois parametros se colocarmos apenas um ou a mais dará erro

print()

print('No python para facilitar a nossa vida temos o que chamamos de empacotamento de parâmetros: ')

# Vamos imaginar que temos um função que temos um contador que contaria quantos números passariamos de parâmetros
def contador(*num):
    tam = len(num)
    for v in num:
        print(v, end=' ')
    print()
    print(f'Recebi os valores {str(num).replace("(", "").replace(")", "")} e são ao todo {tam} números.')
    print()


contador(2, 1, 4)
contador(5, 7)
contador(4, 4, 2, 5)

print('Podemos utilizar mais uma funcionalidade com listas: ')
valores = [7, 2, 5, 0, 4]
print(f'O print de valores é igual: {valores}')

print()

print('Vamos dizer que eu precise de uma função que dobre esse valores chamaremos ela de dobra(): ')
def dobra(lst):
    print(f'O print de valores é igual a: {valores}')
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(f'O print de valores dobrado é igual a: {valores}')
    print()

dobra(valores)

print('Vamos voltas para aquele exemplo de soma:')
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos: {s}')


soma(3, 4)
soma(2, 4, 6, 8)
