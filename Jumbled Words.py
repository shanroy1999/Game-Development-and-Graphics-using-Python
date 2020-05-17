import tkinter
from tkinter import *
import random
from random import shuffle
from tkinter import messagebox

answer = ['machine','google','artificial','yahoo','facebook','apple','microsoft','Twitter']
words = []

for i in answer:
    word = list(i)
    shuffle(word)
    words.append(word)

num = random.randint(0,len(words))

def initial():
    global words, num
    l1.configure(text = words[num])

def ans_check():
    global words,answer,num
    user_input = e1.get()
    if(user_input==answer[num]):
        messagebox.showinfo("Success!", "You are correct!")
        reset()
    else:
        messagebox.showinfo("Sorry", "Please Try Again!")
        e1.delete(0,END)

def reset():
    global answer,words,num
    num = random.randint(0,len(words))
    l1.configure(text=words[num])
    e1.delete(0, END)

win = tkinter.Tk()
win.geometry("300x300")

l1 = Label(win, font="times 20")
l1.pack(pady=30, ipady=10, ipadx=10)

answers = StringVar()
e1 = Entry(win, textvariable=answer)
e1.pack(ipady=5, ipadx=5)

b1 = Button(win, text="Check", width=20, command=ans_check)
b1.pack(pady=40)

b2 = Button(win, text="Reset", width=20, command=reset)
b2.pack()

initial()
win.mainloop()
