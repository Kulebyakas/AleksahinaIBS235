def game():
    answer1 = "слон"
    answer2 = "история"
    answer3 = "юпитер"
    question1 = "Какое животное самое крупное на Земле?"
    question2 = "Как называется наука, которая изучает прошлое?"
    question3 = "Как называется самая большая планета в Солнечной системе?"

    errors = 0
    correct_answers = 0
    question_index = 1

    while errors < 5 and correct_answers < 3:
        
        if question_index == 1:
            user_answer = input(question1 + "\n")
            if user_answer.lower() == answer1:
                print("Правильный ответ!")
                correct_answers += 1
                question_index += 1
                print(correct_answers, question_index)
            else:
                errors += 1
                if errors == 5:
                    print("Вы допустили слишком много ошибок. Игра окончена.")
                print("Неправильный ответ. Попробуйте еще раз.")

        elif question_index == 2:
            user_answer = input(question2 + "\n")
            if user_answer.lower() == answer2:
                print("Правильный ответ!")
                correct_answers += 1
                question_index += 1
            else:
                errors += 1
                if errors == 5:
                    print("Вы допустили слишком много ошибок. Игра окончена.")
                print("Неправильный ответ. Попробуйте еще раз.")

        elif question_index == 3:
            user_answer = input(question3 + "\n")
            if user_answer.lower() == answer3:
                print("Правильный ответ!")
                correct_answers += 1
            else:
                print("Неправильный ответ. Попробуйте еще раз.")
                errors += 1
                if errors == 5:
                    print("Вы допустили слишком много ошибок. Игра окончена.")
            question_index += 1
            if correct_answers == 3:
                print("Вы ответили правильно на все вопросы. Игра окончена.")

game()
