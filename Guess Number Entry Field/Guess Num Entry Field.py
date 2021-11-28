# Guess the Number with Entry Field

#  Guess the Number
#  Program generate random number and user will guess. After each guess a hint will be given

import random
import tkinter as tk
from tkinter import messagebox
import threading


root = tk.Tk()
root.title("Number Guess Game")
root.minsize(width=450, height=250)

f1 = tk.Frame(root, pady=3, bg="#000000")  # frame for quit and start button
f1.pack(expand=True, fill="both")

f2 = tk.Frame(root, pady=3, bg="#000000")  # frame for number of guesses
f2.pack(expand=True, fill="both")

f3 = tk.Frame(root, pady=3, bg="#000000")  # frame for hint
f3.pack(expand=True, fill="both")

f4 = tk.Frame(root, pady=3, bg="#000000")  # frame for number guess
f4.pack(expand=True, fill="both")

f5 = tk.Frame(root, pady=3, bg="#000000")
f5.pack(expand=True, fill="both")

guess = int

def quit():
    msg = tk.messagebox.askyesno("Quit Game", "Would You Like To Quit Game?")
    if msg == True:
        root.destroy()
    else:
        tk.messagebox.showinfo("Return", "You Will Now Continue Playing")

def b1():
    global guess
    guess = int(1)
    num_guess_output.set("1")

def b2():
    global guess
    guess = int(2)
    num_guess_output.set("2")

def b3():
    global guess
    guess = int(3)
    num_guess_output.set("3")

def b4():
    global guess
    guess = int(4)
    num_guess_output.set("4")

def b5():
    global guess
    guess = int(5)
    num_guess_output.set("5")


def play():
    global guess
    ran_num = random.randint(0, 5)  # random number generated
    num_guess_output.set('Please guess a number from 0 to 5')  # user input guess

    if guess == ran_num:  # guess correct
        hint_output.set("Good Guess! You Win!")
        root.destroy()

    elif guess > ran_num:  # guess high
        hint_output.set("Guess is too High")

    elif guess < ran_num:  # guess low
        hint_output.set("Guess is too Low")


# button to quit game
f1_quit = tk.Button(f1, font=("verdana", 15), anchor="center",
                    bg="#5DADE2", text="Quit", command=quit)
f1_quit.pack(side=tk.LEFT, expand=True, fill="both")
# button to start game
f1_start = tk.Button(f1, font=("verdana", 15), anchor="center",
                    bg="#5DADE2", text="Start Here", command=play)
f1_start.pack(side=tk.LEFT, expand=True, fill="both")

# number of guesses output
num_guess_output = tk.StringVar()
num_guess_lbl = tk.Label(f2, font=("verdana", 15), anchor="center",
                    bg="#5DADE2", textvariable=num_guess_output)
num_guess_lbl.pack(expand=True, fill="both")

# hint output
hint_output = tk.StringVar()
hint_output_lbl = tk.Label(f3, font=("verdana", 15), anchor="center",
                    bg="#5DADE2", textvariable=hint_output)
hint_output_lbl.pack(expand=True, fill="both")

# buttons
btn1 = tk.Button(f4, font=("verdana", 15), anchor="center",
                    bg="#5DADE2", text="1", command=b1)
btn1.pack(side=tk.LEFT, expand=True, fill="both")

btn2 = tk.Button(f4, font=("verdana", 15), anchor="center",
                    bg="#5DADE2", text="2", command=b2)
btn2.pack(side=tk.LEFT, expand=True, fill="both")

btn3 = tk.Button(f4, font=("verdana", 15), anchor="center",
                    bg="#5DADE2", text="3", command=b3)
btn3.pack(side=tk.LEFT, expand=True, fill="both")

btn4 = tk.Button(f4, font=("verdana", 15), anchor="center",
                    bg="#5DADE2", text="4", command=b4)
btn4.pack(side=tk.LEFT, expand=True, fill="both")

btn5 = tk.Button(f4, font=("verdana", 15), anchor="center",
                    bg="#5DADE2", text="5", command=b5)
btn5.pack(side=tk.LEFT, expand=True, fill="both")



root.mainloop()

