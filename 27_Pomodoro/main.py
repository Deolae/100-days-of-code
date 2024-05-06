from tkinter import *
import math
import playsound
import random

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
DARKGREEN = "#006400"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
checkmarks = ""
work_done = 0
reps = 0
timer = None
pomodoros = 0
work_quotes = ["Time to work!", "Who's ready for productivity?", "Gotta get the work done, eh?", "You can do it!",
               "Someone's gotta get it done\n that one is you!"]
break_quotes = ["Have a short break,\nyou deserve it!", "Don't get too comfortable now.",
                "Don't go too far now!\n get ready for the next work time.",
                "Take a breather,\n Ready to get back to it?"]


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps, checkmarks, work_done
    window.after_cancel(timer)
    reps = 0
    work_done = 0
    checkmarks = ""
    checkmark_text.config(text=checkmarks)
    canvas.itemconfig(tomato_timer, text="00:00")
    timer_text.config(text="Timer", fg=GREEN)
    motivation_text.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    print(reps)
    # Turn minutes to seconds
    work_sec = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    # if the 8th rep is over, increase pomodoro
    if reps % 9 == 0:
        increase_pomodoros()
        reset_timer()
    # if it's the 8th rep
    elif reps % 8 == 0:
        count_down(long_break_secs)
        timer_text.config(text="Long Break", fg=RED)
        motivation_text.config(text="You've done a pomodoro cycle!\nthis tomato is proud of you.", fg=RED)
    # if it's 2nd/4th/6th rep
    elif reps % 2 == 0:
        count_down(short_break_secs)
        timer_text.config(text="Short Break", fg=PINK)
        motivation_text.config(text=random.choice(break_quotes), fg=PINK)
    # if it's 1st/3rd/5th/7th rep
    else:
        timer_text.config(text="Work Time", fg=GREEN)
        count_down(work_sec)
        motivation_text.config(text=random.choice(work_quotes), fg=DARKGREEN)


# ----------------------- POMODOROS COUNTER MECHANISM ------------------------- #


def increase_pomodoros():
    global pomodoros
    pomodoros += 1
    pomodoros_text.config(text=f"Pomodoros done this session: {pomodoros}")


# ---------------------------- SOUNDS MECHANISM ------------------------------- #


def ten_seconds_sfx():
    playsound.playsound("10_Seconds.wav", False)


def timer_done_sfx():
    playsound.playsound("Digital_alarm.wav", False)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global checkmarks, timer, work_done
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Play the 10 seconds left sounds
    if count_sec == 11:
        ten_seconds_sfx()

    # To have 2 decimal values when seconds are under 10, instead of 1 decimal
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(tomato_timer, text=f"{count_min}:{count_sec}")

    # As long as the timer is above 0, keep counting
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        # Play sfx for timer done
        timer_done_sfx()

        # After every "work time" add a checkmark
        if reps % 2 != 0:
            checkmarks += CHECKMARK
            work_done += 1
            checkmark_text.config(text=f"Work done:{work_done}/4 ({checkmarks})")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

# Create the window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, width=600, height=500)

# Tomato image and timer in center
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
tomato_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)

# "Timer" text above tomato
timer_text = Label(text="Timer", font=(FONT_NAME, 30, "normal"), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer_text.grid(row=0, column=1)

# Reset button
reset_button = Button(text="Reset", command=reset_timer, width=7, pady=2, padx=2)
reset_button.grid(row=2, column=2)

# Start button
start_button = Button(text="Start", command=start_timer, width=7, pady=2, padx=2)
start_button.grid(row=2, column=0)

# Check Marks
checkmark_text = Label(text=f"Work done:{work_done}/4 ()", font=(FONT_NAME, 18, "bold"), fg=GREEN, bg=YELLOW)
checkmark_text.grid(row=3, column=1)

# text under check marks
motivation_text = Label(text="", font=(FONT_NAME, 16, "normal"), fg=DARKGREEN, bg=YELLOW)
motivation_text.grid(row=4, column=1)

# Pomodoros counter
pomodoros_text = Label(text="Pomodoros done this session: 0", font=(FONT_NAME, 16, "normal"), bg=YELLOW)
pomodoros_text.place(x=-80, y=-40)

window.mainloop()
