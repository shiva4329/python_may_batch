from tkinter import *

root = Tk()

Label(root,text="Python Programming",
	   fg = "red",#font color
	   font = "Times").pack() #font style
Label(root, text="JAVA Programming",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").pack()
Label(root, text="C Programming",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold").pack()

root.mainloop()
