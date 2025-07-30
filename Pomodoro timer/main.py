import math
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
reps=0
x=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global x
    window.after_cancel(x)
    canvas.itemconfig(timers,text="00:00")
    timer.config(text="Timer", fg=GREEN)
    check.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec=WORK_MIN * 60
    short_break=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60
    if reps%8==0:
        timer.config(text="Break",fg=RED)
        count_down(long_break)
    elif reps%2==0:
        timer.config(text="Break",fg=PINK)
        count_down(short_break)
    else:
        timer.config(text="Work",fg=GREEN)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global x
    count_min=math.floor(count/60)
    count_sec=count%60
    if 0<=count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timers, text=f"{count_min}:{count_sec}")
    if count>0:
        x=window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        for _ in range(math.floor(reps/2)):
            mark+="✓"
        check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.config(padx=100,pady=50,bg=YELLOW)
window.title("Pomodoro")
timer=Label(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
timer.grid(column=1,row=0)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=img)
timers=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)
start=Button(text="Start",command=start_timer)
start.grid(column=0,row=2)
reset=Button(text="Reset",command=reset_timer)
reset.grid(column=2,row=2)
check=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
check.grid(column=1,row=3)

window.mainloop()
