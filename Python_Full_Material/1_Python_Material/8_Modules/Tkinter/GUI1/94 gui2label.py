from tkinter import *

root = Tk()  #TK is a predefined class
#creating root window, which provides rectangular space on the screen where we
#can display text,components such as labels,buttons

w = Label(root, text="Hello Hyderabad!!")
w.pack()   # to add label to root , pack()method allocates required space to
           #display label on window
root.mainloop() # wait for event,means program execution not finished,untill
                #you press close button on GUI
