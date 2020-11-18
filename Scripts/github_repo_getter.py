import requests

def requisitar_repositorios(headers, query):
    request = requests.post('https://api.github.com/graphql', json = {'query': query}, headers = headers)
    if request.status_code == 200:
        return request.json()
    elif request.status_code == 502:
        return requisitar_repositorios(query, headers)
    else:
        raise Exception("A query falhou: {}. {}".format(request.status_code, query))

def get_repositorios(headers, query):
    response = requisitar_repositorios(headers, query)
    repositorios_retornados = response["data"]["search"]["nodes"]

    print("\nA etapa de recuperação dos repositórios foi finalizada.") 
    return repositorios_retornados