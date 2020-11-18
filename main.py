from Util.header import headers
from Util.query_repos import query_repositorios
from Util.query_issues import query_issues
from Scripts.github_repo_getter import get_repositorios
from Scripts.github_issues_getter import get_issues
from Scripts.exportador_github_infos_csv import exportar_arquivos_csv
from Scripts.stackoverflow_questions_getter import get_questions
from Scripts.exportador_stackoverflow_infos_csv import exportar_questions_csv
from Scripts.analisador_resultados import analisar_resultados
from Scripts.exportador_resultados import exportar_resultados_csv
import pathlib
import os
import shutil

def criar_pasta(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print(f"\nDiretório: {path} não foi criado pois já existe.")
        
def deletar_pasta(path):
    try:
        shutil.rmtree(path)
    except:
        print(f"\nDiretório: {path} não pôde ser excluido. Caso ele exista, favor apagá-lo manualmente.")

def main_script():
    path_questions = str(pathlib.Path().absolute()) + "\\QuestoesStackoverflow"
    path_repositorios_analisados = str(pathlib.Path().absolute()) + "\\RepositoriosAnalisados"
    path_resultados = str(pathlib.Path().absolute()) + "\\resultado_analise_final.csv"
    
    analise_final = []
    
    deletar_pasta(path_questions)
    deletar_pasta(path_repositorios_analisados)
    criar_pasta(path_repositorios_analisados)
    criar_pasta(path_questions)
    
    questions = get_questions(path_questions)
    exportar_questions_csv(questions, path_questions)
    
    repositorios = get_repositorios(headers, query_repositorios)
    
    for i, repositorio in enumerate(repositorios):
        top_issues = get_issues(headers, query_issues, "DESC" , repositorio, path_repositorios_analisados)
        bottom_issues = get_issues(headers, query_issues, "ASC", repositorio, path_repositorios_analisados)
        
        path_repo_analisado = path_repositorios_analisados + "\\" + "{:04n}".format(i+1) + "_" + repositorio['name']
        criar_pasta(path_repo_analisado)
        
        analise_final.append(analisar_resultados(questions, repositorio, top_issues, bottom_issues))
            
        exportar_arquivos_csv(path_repo_analisado, repositorio, top_issues, bottom_issues)
            
        print(f"\nO repositório {repositorio['name']} foi analisado e os resultados retornados foram exportados para um arquivo .csv com sucesso.") 
    
    exportar_resultados_csv(path_resultados, analise_final)       
    
    print("\nO Script foi finalizado com sucesso.")   

main_script()