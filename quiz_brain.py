class QuizBrain:

    def __init__(self, qlist):
        self.question_number = 0
        self.question_list = qlist
        self.score = 0

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q {self.question_number} : {current_question.text}? (True/False) : ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("Wrong")
        print(f"Correct answer is {current_answer}")
        print(f"Your current score is {self.score} / {self.question_number}")
        print("\n")








