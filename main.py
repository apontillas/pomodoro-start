
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
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text='Timer')
    check_label.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text='Long Break', fg=PINK)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text='Short Break', fg=RED)
        count_down(short_break_sec)
    else:
        title_label.config(text='Work', fg=GREEN)
        count_down(work_sec)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sections = math.floor(reps/2)
        for _ in range(work_sections):
            marks += "✔️"
            check_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomorodo Totoro')
window.config(padx=100, pady=50, bg=YELLOW)



#Canvas Widget
canvas = Canvas(width=507, height=614, bg=YELLOW, highlightthickness=0)
totoro_img = PhotoImage(file="totoro.png")
canvas.create_image(250, 300, image=totoro_img)
timer_text = canvas.create_text(250, 400, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

title_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)



start_btn = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(command=reset_timer, text="Reset", highlightthickness=0, highlightbackground=YELLOW)
reset_btn.grid(column=2, row=2)


window.mainloop()
