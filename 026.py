estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('UF: '))
    estado['Sigla'] = str(input('Sigla Estado: '))
    brasil.append(estado.copy())
print(brasil)