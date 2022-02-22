pessoas = list()
dados = list ()

for pessoa in range (0,2):
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Altura: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()

for pessoa in pessoas:

    if(pessoa[2] /(pessoa[1] * pessoa[1]) <= 24.9):
        print(f'{pessoa[2] /(pessoa[1] * pessoa[1])}', end='')
        print(f'{pessoa[0]} não está acima do peso')
    else:
        print(f'{pessoa[2] /(pessoa[1] * pessoa[1])}', end='')
        print(f'{pessoa[0]} está acima do peso')

print(f'{len(pessoas)} pessoas foram cadastradas')
