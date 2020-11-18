import csv

def exportar_questions_csv(questions, path_arquivo_csv):
    path_arquivo_csv += "\\questions_stackoverflow.csv"
    
    with open(path_arquivo_csv, mode='w+') as arquivo_csv:
        csv_writer = csv.writer(arquivo_csv, quotechar='"')
    
        header = (["Question ID", "Quant. views", "Quant. answers", "Score", "Título da Question", "Tags", "Link da Question"])
        csv_writer.writerow(header)
        for question in questions["items"]:
            dict_question_info = {0: question['question_id'], 1: question['view_count'], 2: question['answer_count'],
                                3: question['score'], 4: question['title'], 5: question['tags'], 6: question['link']}
            csv_writer.writerow(dict_question_info.values())