from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
START_BUTTON_COLOR = "#519259"
RESET_BUTTON_COLOR = "#FF865E"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_checkmark.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    global REPS
    REPS += 1

    if REPS % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Long Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=PINK)
        window.attributes("-topmost", True)
    else:
        count_down(work_sec)
        label_timer.config(text="Timer", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    if count >= 0:
        global TIMER
        canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = REPS // 2
        for _ in range(work_sessions):
            marks += "✔"
        label_checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
label_timer.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer, font=(FONT_NAME, 12, "bold"),
                      bg=START_BUTTON_COLOR)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, font=(FONT_NAME, 12, "bold"),
                      bg=RESET_BUTTON_COLOR)
reset_button.grid(column=2, row=2)

label_checkmark = Label(fg=GREEN, bg=YELLOW)
label_checkmark.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
photo = canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
