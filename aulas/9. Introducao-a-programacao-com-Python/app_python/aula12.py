import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/01001000/json/')
    print(response.status_code)
    print(response.text)
    print(type(response.text))

    dados_cep = response.json()
    print(dados_cep['logradouro'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    retorna_dados_cep('01001000')
    dados_pokemon = retorna_dados_pokemon('pikachu')
    print(dados_pokemon['sprites']['front_shiny'])
    response = retorna_response('https://digitalinnovation.one/home')
    print(response)
