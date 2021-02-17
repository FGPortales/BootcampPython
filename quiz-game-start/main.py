from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for v in question_data:
    my_object = Questions(v['text'], v['answer'])
    question_bank.append(my_object)

quiz = QuizBrain(question_bank)

while(quiz.still_has_questions()):
    quiz.next_question()
