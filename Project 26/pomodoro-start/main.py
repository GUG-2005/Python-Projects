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
reps = 1
time = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global reps
    window.after_cancel(time)
    canvas.itemconfig(timer, text="00:00")
    name.config(text="Timer", fg=GREEN)
    reps = 1

def stop_timer():
    window.after_cancel(time)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_min = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        reps += 1
        count_down(long_break)
        name.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        reps += 1
        count_down(short_break)
        name.config(text="Short Break", fg=PINK)
    else:
        reps += 1
        count_down(work_min)
        name.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0"+str(count_sec)

    if count >= 0:
        canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
        global time
        time = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 != 0:
            check.config(text="✔")
        else:
            check.config(text="")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(pady=50, padx=100, bg=YELLOW)

name = Label(text="Timer", fg = GREEN, bg=YELLOW, font=("Times New Roman", 35, 'bold'), highlightthickness=0)
name.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(100, 131, text="00:00", fill="white", font=("Calibiri", 30, 'bold'))
canvas.grid(column=1, row=1)


start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

stop = Button(text="Stop", highlightthickness=0, command=stop_timer)
stop.grid(column=1, row=2, pady=10)

reset = Button(text="Reset", highlightthickness=0, command=reset)
reset.grid(column=2, row=2,)

check = Label(bg=YELLOW, fg=GREEN, font=("Algerian", 20, 'bold'), highlightthickness=0)
check.grid(column=1, row=3)

window.mainloop()