from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for que in question_data:
    que_text = que['text']
    que_answer = que['answer']
    new_question = Question(que_text, que_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You completed the quiz")
print(f"Your final score is {quiz.score} / {quiz.question_number}")
