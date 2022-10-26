import requests


def retorna_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.text)
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    return dados_cep


def retorna_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get('{}'.format(url))
    return response.text

if __name__ == '__main__':
    # retorna_cep(14910000)
    # print(retorna_pokemon('ditto'))
    print(retorna_response('https://assiste.com.br/'))
