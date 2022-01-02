nome = str(input('Qual seu nome completo? ')).lower().strip().split()
print('\033[31mSeu nome tem Silva? {}\033[m'.format('silva' in nome[0::]))
