brasil = []
local = [

    {
    'cidade': 'Maragogipe',
    'estado': 'BA',
    'regiao': 'Nordeste'
    },
    {
    'cidade': 'Salvador',
    'estado': 'BA',
    'regiao': 'Nordeste'
    },
    {
    'cidade': 'Rio de Janeiro',
    'estado': 'RJ',
    'regiao': 'Sudeste'
    },
    {
    'cidade': 'São Paulo',
    'estado': 'SP',
    'regiao': 'Sudeste'
    }
]
for e in local:
    for k,v in e.items():
        print(f'- {k}: {v} \n')