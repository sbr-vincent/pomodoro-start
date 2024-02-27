from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

window.after(1000, )

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
label.grid(column=1, row=0)

checkmark = Label(text="✔", bg=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)

start_button = Button(text="Start", bg="white", highlightthickness=0)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", bg="white", highlightthickness=0)
reset_button.grid(row=2, column=2)



window.mainloop()
