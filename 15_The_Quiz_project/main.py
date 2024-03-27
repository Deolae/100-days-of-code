from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# Fill the questions bank
for question in question_data:
    question_bank.append(Question(text=question["text"],answer=question["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("\nYou've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")