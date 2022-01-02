# Jeito 01
# Criar as listas
parenteses = list()

# Pedir a conta
conta = input('Digite a expressão: ').strip()
for s in conta:
    if s == '(' or s == ')':
        parenteses.append(s)

# Validar a contar
abre_parenteses = parenteses.count('(')
fecha_parenteses = parenteses.count(')')

if abre_parenteses == fecha_parenteses:
    print('Esta ecpressão é válida!')
else:
    print('Esta expressão não é válida!')

# Jeito 02
# Criar as listas
parenteses1 = []
abre_parenteses = 0
fecha_parenteses = 0

# Colocar os parenteses dentro da lista
conta = input('Digite a expressão: ').strip()
for s in conta:
    if s == '(' or s == ')':
        parenteses1.append(s)

# Vendo se a expressão é válida
for p in parenteses1:
    if p == '(':
        abre_parenteses += 1
    elif p == ')':
        fecha_parenteses += 1
print('-=' * 30)
if abre_parenteses == fecha_parenteses:
    print('Esta expressão é válida!')
else:
    print('Esta expressão não é válida!')
