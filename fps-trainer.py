import tkinter
import random
from tkinter import messagebox
from tkinter import scrolledtext

root = tkinter.Tk()
root.title("Simple FPS Trainer")
root.geometry("520x400")
root.configure(bg="grey")

seconds = 20
points = -2

opties = ["Press W", "Press A", "Press S", "Press D", "Press Space", "Single Click", "Double Click",  "Tripple Click"]
gekozen = ["w", "a", "s", "d", "<space>", "<Button>", "<Double-Button>", "<Triple-Button>"]
choice = 5

def start_knop():
    global main_label
    main_label = tkinter.Label(fg = "black", bg = "white", text = "Press here to start")
    main_label.bind(gekozen[5], kiezen)
    main_label.place(x="225", y = "50")

def begin(e):
    global seconds, points, choice
    seconds = 20
    points = -2
    main_label.unbind(opties[5])
    box2.config(text="                                                                                                               0 points")
    choice = random.randint(0,7)
    if choice <= 4:
        root.bind(opties[choice], kiezen)
    else:
        main_label.bind(opties[choice], kiezen)

box1 = tkinter.Label(
    root,
    text="Time remaining: " + str(seconds),
    bg="black",
    fg="white"
)

box1.pack(
    ipadx=10,
    ipady=10,
    side = tkinter.LEFT, 
    anchor = tkinter.N,
)

box2 = tkinter.Label(
    root,
    text="                                                                                                               0 points",
    bg="black",
    fg="white"
)

box2.pack(
    ipadx=10,
    ipady=10,
    side = tkinter.RIGHT,
    anchor = tkinter.N,
)   


def kiezen(e):
    global choice, seconds, points
    main_label.unbind(gekozen[choice])
    main_label.unbind(gekozen[5])
    root.unbind(gekozen[choice])
    main_label.place(x=random.randint(30,490), y=random.randint(30,380))
    if choice <= 4:
        points = points + 1
    else:
        points = points + 2
    choice = random.randint(0, 7)
    main_label['text'] = opties[choice]
    if choice <= 4:
        root.bind(gekozen[choice], kiezen)
    else:
        main_label.bind(gekozen[choice], kiezen)
    box2.config(
        text="                                                                                                               " + str(points) + " points"
    )
    if points == 0:
        timer()
    if points == -1:
        points = 0
        box2.config(text="                                                                                                               0 points")
        timer()


def timer():
    global seconds
    seconds = seconds - 1
    print(seconds)
    box1.config(
        text="Time remaining: " + str(seconds)
    )
    if seconds <= 0:
        global points
        if messagebox.askyesno(title="Time is over!", message="Congratulations you have " + str(points) + " point(s), wanna play again?") == True:
            print("Je hebt ja gekozen")
            main_label.destroy()
            box1.config(text="Time remaining: 20")
            start_knop()
            begin(1)
            return
        else:
            root.destroy()
            print("Je hebt nee gekozen")
    root.after(1000, timer)
# -------------------------------

start_knop()

root.mainloop()