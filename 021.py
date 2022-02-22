a = [2, 3, 5, 9]
b = a #conexão

b[2] = 8
print(f'Lista a {a}')
print(f'Lista b {b}')
b =a[:] #criando copia
b[2] = 0
print(f'Lista a {a}')
print(f'Lista b {b}')