import random

def get_random_question(filename, asked_questions):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            questions = file.readlines()
            available_questions = [q.strip() for q in questions if q.strip() not in asked_questions]
            if available_questions:
                question = random.choice(available_questions)
                asked_questions.add(question)
                return question
            else:
                return None
    except FileNotFoundError:
        return "Файл не найден."

if __name__ == "__main__":
    filename = '[file_address]/questions.txt'
    asked_questions = set()
    
    while True:
        random_question = get_random_question(filename, asked_questions)
        if random_question is None:
            print("Все вопросы были заданы. Выход из программы.")
            break
        elif random_question == "Файл не найден.":
            print(random_question)
            break
        else:
            print(random_question)
        
        user_input = input("Хотите получить еще один вопрос? (да/нет): ").strip().lower()
        if user_input != 'да':
            print("Выход из программы.")
            break