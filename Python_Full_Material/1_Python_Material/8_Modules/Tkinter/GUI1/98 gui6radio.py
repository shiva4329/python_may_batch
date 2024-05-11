from tkinter import *

root = Tk()

v = IntVar()
'''
x = StringVar() # Holds a string; default value ""
x = IntVar() # Holds an integer; default value 0
x = DoubleVar() # Holds a float; default value 0.0
x = BooleanVar() # Holds a boolean, returns 0 for False and 1 for True
'''
Label(root, text="""Choose a programming language:""",
      justify = LEFT,
      padx = 20).pack()
Radiobutton(root, 
            text="PYTHON",
            padx = 20,
            variable=v,
            value=1).pack(anchor=W) 
Radiobutton(root, 
            text="JAVA",
            padx = 20,
            variable=v,
            value=2).pack(anchor=W)

mainloop()

'''
various options:
1)justify :If the text contains multiple lines, this option controls how the text is justified:
            CENTER (the default), LEFT, or RIGHT.
	
2)padx :How much space to leave to the left and right of the radiobutton and text. Default is 1.
	
3)pady :How much space to leave above and below the radiobutton and text. Default is 1.

4)text : The label displayed next to the radiobutton.

5)value :When a radiobutton is turned on by the user, its control variable is set to its current value option.
         If the control variable is an IntVar, give each radiobutton in the group a different integer value option.
         If the control variable is a StringVar, give each radiobutton a different string value option.
	
6)variable :The control variable that this radiobutton shares with the other radiobuttons in the group.
          This can be either an IntVar or a StringVar.



Anchors are used to define where text is positioned relative to a reference point.

Here is list of possible constants, which can be used for Anchor attribute.

NW---->north west
N----->north
NE---->north east
W----->west
CENTER->Center
E------>East
SW----->south west
S------>south
SE----->south east

NW     N      NE


W    CENTER   E


SW     S      SE

'''








