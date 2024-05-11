'''Entry widgets are used to get input, i.e. text strings, from the user of an application.
This widget allows the user to enter a single line of text. If the user enters a string,
which is longer than the available display space of the widget, the content will be scrolled.
This means that the string cannot be seen in its entirely.
The arrow keys can be used to move to the invisible parts of the string.
If you want to enter multiple lines of text, you have to use the text widget.
An entry widget is also limited to single font.''' 

from tkinter import *

master = Tk()
Label(master, text="First Name:").grid(row=0)
Label(master, text="Last Name:").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

mainloop( )
