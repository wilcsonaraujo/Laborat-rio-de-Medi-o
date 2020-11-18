from stackapi import StackAPI
import html

def tags_to_string(tags):
    tags_concatenadas = ""
    for tag in tags:
        tags_concatenadas += f"{tag}, "
    return tags_concatenadas.rstrip(', ')

def get_questions(path):
    conseguiu_recuperar = False
    while(conseguiu_recuperar is False):
        try:
            STACK_SITE = StackAPI('stackoverflow')
            STACK_SITE.max_pages=1
            top_viewed_questions = STACK_SITE.fetch('questions', sort='votes', order='desc')
            conseguiu_recuperar = True
        except:
            print("\nOcorreu um erro no momento de recuperar as questions pela API do Stackoverflow. Tentando novamente...\n")
    
    for question in top_viewed_questions["items"]:
        question['tags'] = tags_to_string(question['tags'])
        question['title'] = html.unescape(question['title'])
    
    return top_viewed_questions
