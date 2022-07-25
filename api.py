import requests
import json

def requisicao(titulo):
try:
    req = requests.get('http://www.omdbapi.com/?t=' + titulo)
    dicionario = json.loads(req.text)
    return dicionario
except:
    print('Erro na conexão')
    return None

    def printar_detalhes(filme):
    print(dicionario)
    print('Titulo:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actores'])
    print('Nota:', filme['Notes'])

    sair = False
    while not sair:
        op = input('Escreva um nome de um filme ou sair para fechar: ')

        if op == 'Sair':
            sair = True
        else:
            filme = requisicao(op)
            if filme['Response'] == False:
                print('Filme não encontrado')
            else:
                printar_detalhes(filme)
