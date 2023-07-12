# TODO 1: ask the question
# TODO 2: check the answer
# TODO 3: check if is the end of the quiz

class QuizBrain:
    def __init__(self, bank_of_question):
        self.question_number = 0
        self.bank_of_question = bank_of_question
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.bank_of_question)

    def next_question(self):
        current_question = self.bank_of_question[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q{self.question_number}. {current_question.text}: (True or False): ')
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('Correct answer!')
        else:
            print("That's wrong.")
        print(f'the correct answer is: {correct_answer}')
        print(f'Your score is {self.score}/{len(self.bank_of_question)}')
        print('\n')

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer