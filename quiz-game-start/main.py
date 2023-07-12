from data import question_data
from quiz_brain import QuizBrain, Question

question_bank = []
for data in question_data:
    question_bank.append(Question(data['question'], data['correct_answer']))


quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"You've completed the quiz")
print(f"You final score was: {quiz_brain.score}/{len(quiz_brain.bank_of_question)}")
