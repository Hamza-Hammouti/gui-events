import tkinter

window = tkinter.Tk()
window.title("Clicker")
window.geometry("250x180")
window.configure(bg="grey")

number = 0
kleur = 0
status = ""

def up():
    global number, kleur, status
    number += 1
    status = "up"
    if number >= 1:
        window.configure(bg="green")
        kleur = 1
    elif number == 0:
        window.configure(bg="grey")
        kleur = 0
    button2["text"] = (number)

def down():
    global number, kleur, status
    number -= 1
    status = "down"
    if number <= -1:
        window.configure(bg="red")
        kleur = 2
    elif number == 0:
        window.configure(bg="grey")
        kleur = 0
    button2["text"] = (number)

def on_enter(e):
    window.configure(bg="yellow")

def on_leave(e):
    if kleur == 0:
        window.configure(bg='grey')
    elif kleur == 1:
        window.configure(bg="green")
    elif kleur == 2:
        window.configure(bg="red")  

def multiplier(e):
    global status, number
    if status == "up":
        number = number * 3
    elif status == "down":
        number = number / 3
    number = round(number,2)
    button2.config(text=number)

def update(self):

    self.label.configure(text=self.time_string())

    # schedule another timer
    self.label.after(1000, self.update)

button1 = tkinter.Button(window, text ="Up", width="30", command=up)
button1.grid(row=0, column=0, padx=15, pady=15)
button2 = tkinter.Label(window, text = number, width="30")
button2.grid(row=1, column=0, padx=15, pady=15)
button3 = tkinter.Button(window, text ="Down", width="30", command=down)
button3.grid(row=2, column=0, padx=15, pady=15)

button2.bind("<Enter>", on_enter)
button2.bind("<Leave>", on_leave)
button2.bind("<Double-Button-1>", multiplier)

# -------------------------------

window.mainloop()