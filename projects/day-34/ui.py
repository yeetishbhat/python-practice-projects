from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
from tkinter import *

class QuizInterface:
    def __init__(self , quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lable = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_lable.grid(row=0, column=1)

        self.canvas = Canvas(width=300 , height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=1)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="some text" ,
            fill=THEME_COLOR,
            font = ("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0 , columnspan=2, pady=50)

        ture_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=ture_image, highlightthickness=0, command= self.check_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button( image= false_image ,command= self.check_false)
        self.false_button.grid(row=2, column=1)

        self.next_question()


        self.window.mainloop()


    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_lable.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "the quiz is over")
            self.score_lable.config(text=f"your final score: {self.quiz.score}")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def check_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)






