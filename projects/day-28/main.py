from pickle import GLOBAL
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_main = None

# ---------------------------- TIMER RESET ------------------------------- #4
def reset_timer():
    window.after_cancel(timer_main)
    global reps
    reps = 0
    canvas2.itemconfig(session, text=f"Timer", fill=GREEN)
    canvas1.itemconfig(timer, text=f"00:00")
    checkmark.config(text="")



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    work = WORK_MIN*60
    if reps % 8 == 0:
        canvas2.itemconfig(session, text=f"long break", fill=GREEN)
        count_down(long_break)
    elif reps % 2 == 0:
        canvas2.itemconfig(session, text=f"short break",    fill=GREEN)
        count_down(short_break)
    else:
        canvas2.itemconfig(session, text=f"work",fill=RED)
        count_down(work)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas1.itemconfig(timer , text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_main
        timer_main = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for reps in range(work_session):
            mark += "✓"
        checkmark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.configure(padx=100, pady=50, bg= YELLOW)

canvas1 = Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas1.create_image(100, 112, image=tomato_img)
timer = canvas1.create_text(102, 130,text= "00:00",fill="white",font=(FONT_NAME,28,"bold"))
canvas1.grid(row=1, column=1)

canvas2 = Canvas(width=200, height=100, bg=YELLOW, highlightthickness=0)
session = canvas2.create_text(100, 40,text= "TIMER",fill=GREEN,font=(FONT_NAME,50,"bold"))
canvas2.grid(row=0, column=1)

start = Button(text="start",highlightthickness=0 ,command=start_timer)
start.grid(row=2, column=0)

reset = Button(text= "reset",highlightthickness=0 ,command = reset_timer)
reset.grid(row=2, column=3)

checkmark = Label(fg=GREEN,bg=YELLOW)
checkmark.grid(row=3, column=1)


window.mainloop()

