# palindromo

frase = 'anotaram a data da maratona1'
# palavras = frase.split()
# juntar = ''.join(palavras) // Junta palavras
novafrase = ''
novafrase = frase.strip().upper().replace(' ','')
inverter = ''
for letra in range(len(novafrase) - 1, -1, -1):
    inverter += novafrase[letra]

if inverter == novafrase:
    print('É um Palindromo')
else:
    print('Não é um Palindromo')