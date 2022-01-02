s, valores = 0, 0
for cont in range(3, 501, 3):
    if cont % 2 == 1:
        s += cont
        valores += 1
print(f'A soma dos {valores} valores solicitados é de: {s}')
