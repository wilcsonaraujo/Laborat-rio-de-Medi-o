import requests

def requisitar_issues(headers, query, nome_repositorio, path_repositorios_analisados):
    try:
        request = requests.post('https://api.github.com/graphql', json = {'query': query}, headers = headers)
        if request.status_code == 200:
            return request.json()
        elif request.status_code == 502:
            return requisitar_issues(query, headers, nome_repositorio, path_repositorios_analisados)
        else:
            raise Exception("A query falhou: {}. {}".format(request.status_code, query))
    except:
        erro = f"\nOcorreu um erro com a API do GitHub e as issues do repositório {nome_repositorio} não puderam ser obtidas."
        escrever_log_erro(erro, path_repositorios_analisados)
        print(erro)
            
def escrever_log_erro(erro, path_repositorios_analisados):
    path_arquivo_erro = path_repositorios_analisados + "\\log_erros.txt"
    with open(path_arquivo_erro, "a+") as myfile:
        myfile.write(erro)         

def get_issues(headers, query_issues, orientacao_ordenacao, repositorio, path_repositorios_analisados):
    nome_owner_repositorio = repositorio['nameWithOwner'].split('/')
    owner_repositorio = nome_owner_repositorio[0]
    nome_repositorio = nome_owner_repositorio[1]

    query_issues_final = query_issues.replace("{placeholder_nome_repo}", nome_repositorio)
    query_issues_final = query_issues_final.replace("{placeholder_owner_repo}", owner_repositorio)
    query_issues_final = query_issues_final.replace("{placeholder_orientacao_issue}", orientacao_ordenacao)
    
    response = requisitar_issues(headers, query_issues_final, nome_repositorio, path_repositorios_analisados)
    
    issues_retornadas = []
    
    if(response is not None):
        issues_retornadas = response["data"]["repository"]["issues"]["nodes"]
    
    return issues_retornadas