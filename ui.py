from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 12, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        # canvas
        self.canvas_question = Canvas(width=300, height=250, bg="white")
        self.canvas_question_text = self.canvas_question.create_text(150, 125, width=280, font=FONT,
                                                                     fill="black", anchor=CENTER, text="")
        self.canvas_question.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        # buttons
        self.wrong = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=self.wrong, command=self.false_pressed)
        self.wrong_button.grid(column=1, row=2)

        self.right = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=self.right, command=self.true_pressed)
        self.right_button.grid(column=0, row=2)

        # labels
        self.score_label = Label(text="Score: ", font=("Arial", 15, "italic"), bg=THEME_COLOR,
                                 fg="white")
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas_question.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas_question.itemconfig(self.canvas_question_text, text=question_text)
        else:
            self.canvas_question.itemconfig(self.canvas_question_text, text="The end!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas_question.config(bg="green")
        else:
            self.canvas_question.config(bg="red")
        self.window.after(1000, self.get_next_question)
