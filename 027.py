aluno = dict()
aluno['nome'] = str(input('Insira seu nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno["media"] >= 5:
    aluno['situacao'] = 'Aprovado'
elif aluno["media"] < 5:
    aluno['situacao'] = "Recoperação"
print('-='*30)
for key, value in aluno.items():
    print(f'{key} = {value}')