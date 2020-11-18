import csv

def exportar_resultados_csv(path_arquivo_csv, resultados):
    with open(path_arquivo_csv, mode='w+') as arquivo_csv:
        csv_writer = csv.writer(arquivo_csv, quotechar='"')
        header = (["Nome repositório", "Linguagem primária", "Qt. menções da LP nas quest. do SO",
                    "Qt. menções da LP nas quest. do SO s/ repetição", "Qt. menções do título das top issues nas quest. do SO",
                    "Qt. respostas da questions relacionadas as top issues", "Score das questions relacionadas as top issues",
                    "Qt. menções do título das bottom issues nas quest. do SO",  "Qt. respostas da questions relacionadas as bottom issues",
                    "Score das questions relacionadas as bottom issues"])
        
        csv_writer.writerow(header)
        
        for linha in resultados:
            linha_splitada = linha.split(",")
            
            dict_resultado = {0: linha_splitada[0], 1: linha_splitada[1], 2: linha_splitada[2],
                              3: linha_splitada[3], 4: linha_splitada[4], 5: linha_splitada[5],
                              6: linha_splitada[6], 7: linha_splitada[7], 8: linha_splitada[8],
                              9: linha_splitada[9]}
            
            csv_writer.writerow(dict_resultado.values())