
soma = int(0)
for i in range (1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
        print('{}'.format(soma))
    if i == 0:
        print('Okay')
print('O total da soma e: {}'.format(i))