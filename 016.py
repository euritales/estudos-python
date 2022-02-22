frase = str(input('Insira uma frase: ')).strip()
caracter = str(input('Insira um caracter para ser buscado: ')).strip()

print('O caracter {} aparece na frase {} vezes '.format(caracter, frase.count(caracter)))
print('O caracter {} aparece por ultimo na posição {}  '.format(caracter, frase.rfind(caracter)+1))
print('O caracter {} aparece por primeiro na posição {} '.format(caracter, frase.find(caracter)+1))
