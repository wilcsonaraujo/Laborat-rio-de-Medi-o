import csv
import re

def corrige_formatacao_title_issue(issue):
    if issue.get('title') is not None: 
        regex_pattern = re.compile(r'[^\x00-\x7F]+')
        issue['title'] = re.sub(regex_pattern, '', issue['title'])    
    else:
        issue['title'] = "O título desta issue é vazio"

def primary_language_dict_to_string(repo):
    if repo.get('primaryLanguage') is not None:        
        for key,val in repo.get('primaryLanguage').items():
            repo['primaryLanguage'] = str(val)
    else:
        repo['primaryLanguage'] = "Linguagem não definida"
        
def comments_dict_to_string(issue):
    if issue.get('comments') is not None:        
        for key,val in issue.get('comments').items():
            issue['comments'] = str(val)
    else:
        issue['comments'] = "0"
    
def exportar_infos_repositorio(repositorio, path_arquivo_csv):
    primary_language_dict_to_string(repositorio)
    with open(path_arquivo_csv, mode='w+') as arquivo_csv:
        csv_writer = csv.writer(arquivo_csv)
        
        header = (["Nome", "Owner", "Linguagem Primária"])
        csv_writer.writerow(header)
        
        nome_owner_repositorio = repositorio['nameWithOwner'].split('/')
        dict_repo_info = {0: nome_owner_repositorio[1], 1: nome_owner_repositorio[0], 2: repositorio['primaryLanguage']}
        csv_writer.writerow(dict_repo_info.values())

def exportar_infos_issues(issues, path_arquivo_csv):
    with open(path_arquivo_csv, mode='w+') as arquivo_csv:
        csv_writer = csv.writer(arquivo_csv)
    
        header = (["Número da Issue", "ID", "Quant. comentários", "Título"])
        csv_writer.writerow(header)
    
        for issue in issues:
            comments_dict_to_string(issue)
            corrige_formatacao_title_issue(issue)
            
            dict_issue_info = {0: issue['number'], 1: issue['id'], 2: issue['comments'], 3: issue['title']}
            csv_writer.writerow(dict_issue_info.values())

def exportar_arquivos_csv(path_repo_analisado, repositorio, top_issues, bottom_issues):
    path_arquivo_csv_repo = path_repo_analisado + "\\repositorio_info.csv"
    path_arquivo_csv_top_issues = path_repo_analisado + "\\top_issues_info.csv"
    path_arquivo_csv_bottom_issues = path_repo_analisado + "\\bottom_issues_info.csv"
    
    exportar_infos_repositorio(repositorio, path_arquivo_csv_repo)
    
    if(len(top_issues) > 0):
        exportar_infos_issues(top_issues, path_arquivo_csv_top_issues)
        
    if(len(bottom_issues) > 0):
        exportar_infos_issues(bottom_issues, path_arquivo_csv_bottom_issues)