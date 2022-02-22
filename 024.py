dados = dict()
dados = {
    'nome': 'Pedro',
    'idade': 25
}
print(dados['nome'], dados['idade'])
dados['sexo'] = 'M'

for k,v in dados.items():
    print(f'O {k} é {v}')

# for k in dados.items():
#     print(f'{k} ')
# for k in dados.values():
#     print(f'{k} ')
# for k in dados.keys():
#     print(f'{k} ')

# print(dados)
# del dados['sexo']
# print(f'{dados}')
