from tkinter import *

root = Tk()

v = IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
]

def ShowChoice():
    print(v.get())

Label(root, 
      text="""Choose your favourite programming language:""",
      justify = LEFT,
      padx = 20).pack()

for txt, val in languages:
    Radiobutton(root, 
                text=txt,
                indicatoron=0,
                padx = 20, 
                variable=v, 
                command=ShowChoice,
                value=val).pack(anchor=W)

mainloop()

'''Instead of having radio buttons with circular holes containing white space,
we can have radio buttons with the complete text in a box.
We can do this by setting the indicatoron (stands for "indicator on") option to
0, which means that there will be no separate radio button indicator.
The default is 1.'''






