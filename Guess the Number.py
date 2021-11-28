# Guess the Number with Entry Field

#  Guess the Number
#  Program generate random number and user will guess. After each guess a hint will be given

import random
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Number Guess Game")
root.minsize(width=450, height=250)


guess_num = StringVar()
hint = StringVar()

def start():
    global ran_num
    ran_num = random.randint(0, 5)  # random number generated
    hint.set("Enter a Number 0 to 5")


def play():
    global ran_num
    guess = int(guess_num.get())
    if guess == ran_num:
        hint.set("Good Job! You Win!")
    elif guess > ran_num:  # guess high
        hint.set("Guess is too High")
        entry.delete(0, END)
    elif guess < ran_num:  # guess low
        hint.set("Guess is too Low")
        entry.delete(0, END)



def quit():
    msg = messagebox.askyesno("Quit Game", "Would You Like To Quit Game?")
    if msg == True:
        root.destroy()
    else:
        messagebox.showinfo("Return", "You Will Now Continue Playing")


f0 = Frame(root, pady=3, bg="#000000")  # frame 1 for start instructions
f0.pack(expand=True, fill="both")
# hint label
title = Label(f0, font=("verdana", 12, "italic"), anchor="center",
                    bg="#5DADE2", text="---Press 'Start Game' to Play---", )
title.pack(expand=True, fill="both", pady=3, padx=8)

f1 = Frame(root, pady=3, bg="#000000")  # frame 2 for lives
f1.pack(expand=True, fill="both")
"""
lives_lbl = Label(f1, font=("verdana", 18, "italic"), anchor="center",
                    bg="#5DADE2", textvariable=lives)
lives_lbl.pack(expand=True, fill="both", pady=3, padx=6)
"""
f2 = Frame(root, pady=3, bg="#000000")  # frame for number of guesses
f2.pack(expand=True, fill="both")

# entry field
entry = Entry(f2, font=("verdana", 15), relief=SUNKEN, border=10,
                bg="#D5D8DC", text="Submit", width=15,
              textvariable=guess_num)
entry.pack(side=LEFT, expand=True, fill="y",)

# submit button
submit_btn = Button(f2, font=("verdana", 15), anchor="center", relief=GROOVE, border=10,
                    bg="#5DADE2", text="Submit", command=play)
submit_btn.pack(side=LEFT, expand=True, fill="both", pady=3, padx=8)

f3 = Frame(root, pady=3, bg="#000000")  # frame for hint
f3.pack(expand=True, fill="both")

# hint label
hint_lbl = Label(f3, font=("verdana", 18), anchor="center", relief=SUNKEN, border=10,
                    bg="#5DADE2",
                 textvariable=hint)
hint_lbl.pack(expand=True, fill="both", pady=3, padx=8)

f4 = Frame(root, pady=3, bg="#000000")  # frame for number guess
f4.pack(expand=True, fill="both")

# button to quit game
quit = Button(f4, font=("verdana", 15), anchor="center", relief=GROOVE, border=10,
                    bg="#D2B4DE", text="Quit", command=quit)
quit.pack(side=LEFT, expand=True, fill="both", pady=3, padx=6)

# button to start game
start = Button(f4, font=("verdana", 15), anchor="center", relief=GROOVE, border=10,
                    bg="#D2B4DE", text="Start Game", command=start)
start.pack(side=LEFT, expand=True, fill="both", pady=3, padx=6)


# number of guesses output
num_guess_output = StringVar()
num_guess_lbl = Label(f2, font=("verdana", 15), anchor="center",
                    bg="#5DADE2", textvariable=num_guess_output)
num_guess_lbl.pack(expand=True, fill="both")



root.mainloop()

