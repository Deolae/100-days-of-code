from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # Window
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(width=450, height=650, bg=THEME_COLOR, pady=20,padx=20)
        self.window.title("Osama's Quizzler")

        # Score
        self.score_text = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", pady=20, font=("arial", 16, "normal"))
        self.score_text.grid(row=0, column=1)

        # Buttons
        self.tick_image = PhotoImage(file="images/true.png")
        self.tick_button = Button(image=self.tick_image, borderwidth=0, command=self.true_answer)
        self.tick_button.grid(row=2, column=0)
        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, borderwidth=0, command=self.false_answer)
        self.wrong_button.grid(row=2, column=1)

        # Middle Canvas
        self.canvas = Canvas(width=350,height=250, bg="white")
        self.question_text = self.canvas.create_text(175,125,width=290, text="Question goes here...", font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2, pady=40)
        self.get_next_question()

        # Main loop
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Congrats, you've finished the quiz!"
                                                            f"\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.wrong_button.config(state="disabled")
            self.tick_button.config(state="disabled")

# For the following next 2 functions:
    # Check if the answer is true or false and color the background based on it
    # Sleep for 1 second, to give the user a chance to see the feedback
    # Move onto the next question and update the score
    def true_answer(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_answer(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#90EE90")
        else:
            self.canvas.config(bg="#FF7F7F")

        self.window.after(500, self.get_next_question)
        self.score_text.config(text=f"Score: {self.quiz.score}")