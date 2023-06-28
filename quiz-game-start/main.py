from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_bank.append(Question('text', 'answer'))

quiz_brain = QuizBrain(question_bank)
quiz_brain.next_question()