import random

def get_random_question(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            questions = file.readlines()
            if questions:
                return random.choice(questions).strip()
            else:
                return "Файл с вопросами пуст."
    except FileNotFoundError:
        return "Файл не найден."

if __name__ == "__main__":
    filename = '[file_address]/questions.txt'
    
    while True:
        random_question = get_random_question(filename)
        print(random_question)
        
        user_input = input("Хотите получить еще один вопрос? (да/нет): ").strip().lower()
        if user_input != 'да':
            print("Выход из программы.")
            break