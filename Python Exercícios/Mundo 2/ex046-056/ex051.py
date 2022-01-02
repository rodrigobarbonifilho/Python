print(30*'=')
print(f'{"10 TERMOS DE UMA P.A.": ^30}')
print(30*'=')
termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = termo + (10 - 1) * razao
cont = 1
for n in range(termo, decimo + razao, razao):
    if cont < 10:
        cont += 1
        print(n, end=' -> ')
print('ACABOU!')