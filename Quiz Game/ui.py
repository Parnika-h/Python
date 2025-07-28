from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, highlightthickness=0, bg="white")
        self.question = self.canvas.create_text(
            150, 125,
            width=250,
            text="Questions",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        tick_img = PhotoImage(file="./images/true.png")
        wrong_img = PhotoImage(file="./images/false.png")

        self.tick = Button(image=tick_img, highlightthickness=0, command=self.true)
        self.tick.image = tick_img
        self.tick.grid(column=0, row=2)

        self.wrong = Button(image=wrong_img, highlightthickness=0, command=self.false)
        self.wrong.image = wrong_img
        self.wrong.grid(column=1, row=2)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_q():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.ask()
            self.canvas.itemconfig(self.question, text=question_text)
        else:
            self.canvas.itemconfig(self.question, text="End of Quiz")
            self.tick.config(state="disabled")
            self.wrong.config(state="disabled")

    def true(self):
        is_right = self.quiz.check_ans("True")
        self.give_feedback(is_right)

    def false(self):
        is_right = self.quiz.check_ans("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)
