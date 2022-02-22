dados = list()
pessoas = list()
maior = menor = 0

for info in range (0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()

for usuario in pessoas:
    if usuario[1] >= 18:
        print(f'{usuario[0]} é maior de idade')
        maior += 1
    else:
        print(f'f{usuario[0]} é menor de idade')
        menor += 1

print(f'Houveram {maior} maiores e {menor} menores')

