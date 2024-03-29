class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        no_of_questions = len(self.question_list)
        questions_left = no_of_questions - self.question_number
        if questions_left > 0:
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        users_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ")
        self.check_answer(users_answer, current_question.answer)
        self.question_number += 1

    def check_answer(self, users_answer, correct_answer):
        if users_answer.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number+1}\n")
