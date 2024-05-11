'''drawing text on top of the image , for that We need just one label and use the image and the
text option at thesame time. By default, if an image is given, it is drawn instead of the text.
To get the text as well,you have to use the compound option.
If you set the compound option to CENTER the text will be drawn on the image:'''

import tkinter as tk


root = tk.Tk()
logo = tk.PhotoImage(file="/home/shivakandi/DigitalNest/Python/1_Python_Material/GUI2/Python logo2.gif")

#w1 = tk.Label(root, image=logo).pack(side="right")

description = """Python is a User-friendly programming language
that provides simple and easy syntaxes.

Note: At present, only GIF and PPM/PGM
formats are supported.In coming versions
all formats will be supported"""

w2 = tk.Label(root, 
              compound=tk.CENTER,
              text=description,
              image=logo).pack()
'''w3 = tk.Label(root, 
          #justify=tk.LEFT,
          compound = tk.LEFT,
          padx = 10, 
          text=description, 
          image=logo).pack(side="right")'''
root.mainloop()


