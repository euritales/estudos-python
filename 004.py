a = input('Digite algo:')
print('O tipo do valor inserido é:', type(a))


if a.isspace():
    print('Só existem espaços')
elif a.isnumeric():
    print('O tipo do conteudo ({}) é um numerico.'.format(a), type(a))
elif a.isalpha():
    print('O tipo do conteudo ({}) é um alfabetico.'.format(a))
    print('Esta minusculo?', a.islower())
    print('Esta maiusculo?', a.isupper())
    print('Esta minusculo?', a.islower())
    print('Esta capitalizada(Maiuscula e minuscula)?', a.istitle())
elif a.isalnum():
    print('O tipo do conteudo ({}) é um alfanumerico.'.format(a))
    print('Esta minusculo?', a.islower())
    print('Esta maiusculo?', a.isupper())
    print('Esta capitalizada(Maiuscula e minuscula)?', a.istitle())
