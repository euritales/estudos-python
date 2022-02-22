comida = ['Carne','Lasanha','Feijão', 'suco', 'pizza', 'hamburguer']
num = [1, 4, 2, 5, 3, 34, 324, 2, 23, 2, 0]
print(f'{num}')
num.append(13)
print(f'{num}')
num.sort()
print(f'{num}')
num.sort(reverse=True)
print(f'{num}')
print(f'Tamanho da lista:{len(num)}')
num.insert(1, 1000)
print(f'{num}')
num.pop()
print(f'{num}')
num.pop(1)
print(f'{num}')
print('for')

for i in range (0, len(num)):
    print(f'{num[i]}...', end='')
    print(f'Lugar:{i}')
    if num[i] % 2 == 0:
        print('Par')
        print(f'tamanho:{len(num)}')

print(f'{num}')
