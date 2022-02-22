num = (
    int(input('Digite um numero')),
    int(input('Digite mais um numero')),
    int(input('Digite mais um numero')),
    int(input('Digite mais um numero')),
)

print(f'Voce digitou os numeros: {num}')
print(f'O numero {num[1]} apareceu {num.count(num[1])} vezes')
print(f'O numero {num[2]} apareceu na posicao {num.index(num[2])+1}')
print('Numeros pares:')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
