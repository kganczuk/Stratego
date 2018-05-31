from tkinter import *
import Player

def button():
    print(E1.get(), E2.get())

top = Tk()
F1 = Frame(top)
F1.pack()
L1 = Label(F1, text="Red Player", width=20, fg='red')
L1.pack(side=LEFT)
E1 = Entry(F1, bd =5)
E1.pack(side=RIGHT)
F2 = Frame(top)
F2.pack()
L2 = Label(F2, text="Blue Player", width=20, fg='blue')
L2.pack(side=LEFT)
E2 = Entry(F2, bd =5)
E2.pack(side=RIGHT)

B = Button(top, text="Start", command=button)
B.pack()

top.mainloop()