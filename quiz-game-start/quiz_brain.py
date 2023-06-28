# TODO 1: ask the question
# TODO 2: check the answer
# TODO 3: check if is the end of the quiz

class QuizBrain:
    def __init__(self, bank_of_question):
        self.question_number = 0
        self.bank_of_question = bank_of_question

    def next_question(self):
        current_question = self.bank_of_question[self.question_number]
        input(f'Q{self.question_number} {current_question.text}: (True or False): ')

