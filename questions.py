from dataclasses import dataclass


@dataclass
class Question:
    text: str
    answers: list[str]
    rigth_answer_index: int
    explanation: str | None = None
    rigth_answers_indexes: list[int] | None = None
    

    @property
    def rigth_answer(self):
        return self.answers[self.rigth_answer_index]

questions = [
    Question(text = "Сколько было найдено планет за пределами Солнечной системы?",
            answers=["< 1k", "1k - 10k", "10k - 1kk", "> 1kk",],
            rigth_answer_index=1,
            explanation='Планеты искать сложно'),
    Question(text = "Сколько лет Земле?",
            answers=["2023", "8000", "6.5ккк", "Земли не существует"],
            rigth_answer_index=2),
    Question(text = "Солнце является ...",
            answers=["Белым карликом", "Желтым карликом", "Солнца не сущесвует", "Красным гигантом"],
            rigth_answer_index=1),
]


def main():
    from time import sleep

    for question in questions:
        print(question.text)
        print(*question.answers, sep='\n')
        answer = input('Введите ваш ответ: ')
        sleep(0.5)
        if answer != question.rigth_answer:
            print('Неправильный ответ')
            print(f'правильный ответ {question.rigth_answer}')
            if question.explanation:
                print(question.explanation)
        sleep(5)
        
if __name__ == '__main__':
    main()