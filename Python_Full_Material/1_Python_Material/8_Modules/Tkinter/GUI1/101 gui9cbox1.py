from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text="TELUGU", variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text="ENGLISH", variable=var2).grid(row=1, sticky=W)
var3 = IntVar()
Checkbutton(master, text="HINDI", variable=var3).grid(row=2, sticky=W)
mainloop()
