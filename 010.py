n = int(input('insira um numero: '))
primo = int(0)
for i in range(1, n+1):
    if n % i == 0:
        primo += 1
if primo == 2:
    print('O numero inserido é primo: {}'.format(primo))
else:
    print('O numero inserido não é primo: {}'.format(primo))
