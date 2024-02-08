from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for text in question_data:
    question_text = text["text"]
    answer_text = text["answer"]
    new_question = Question(question_text, answer_text)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"You've completed the quiz. Your final score was {quiz.score}/{len(question_bank)}")