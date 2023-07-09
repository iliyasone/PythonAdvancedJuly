questions = [
    {'text': "Сколько было найдено планет "
             "за пределами Солнечной системы?",
     'answers': ["< 1k", "1k - 10k", "10k - 1kk", "> 1kk",],
     'rigth_answer_index': 1,
     'explanation' : None    
    },
    
    {'text': "Сколько лет Cолнцу?",
     'answers': ["< 1k", "1k - 10k", "10k - 1kk", "> 1kk",],
     'rigth_answer_index': 3,
     'explanation' : None    
    }
]

for question in questions:
    print(question['text'])
    print(*question['answers'],sep='\n')
    answer_from_user = input()
    rigth_answer_index = question['rigth_answer_index']
    if answer_from_user != question['answers'][rigth_answer_index]:
        print(f"Неправильно! Правильный ответ {question['answers'][rigth_answer_index]}")



question = {
    'text' : 'текст вопроса',
    'answers': ['а', 'б', 'в'],
    'right_answer_index' : 0,
    'explanation' : 'объяснение'
 }