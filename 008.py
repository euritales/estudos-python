lista = [ 2, 16, 32, 23, 17, 64]
soma = 0
for i in range(6):
    if lista[i] % 2 == 0:
        soma += lista[i]
        print('Soma: {}'.format(soma))

