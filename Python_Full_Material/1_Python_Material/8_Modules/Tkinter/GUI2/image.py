#labels can contain text and images. The following example contains two labels,
#one with a text and the other one with an image. 
import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="/home/shivakandi/DigitalNest/Python/1_Python_Material/GUI2/Python logo2.gif")
                           
                           
w1 = tk.Label(root, image=logo).pack(side="right")

description = """Python is a User-friendly programming language
that provides simple and easy syntaxes.

Note: At present, only GIF and PPM/PGM
formats are supported.In coming versions
all formats will be supported"""

w2 = tk.Label(root, 
              justify=tk.LEFT,
              padx = 10, 
              text=description).pack(side="left")
root.mainloop()


'''The "justify" parameter can be used to justify a text on the LEFT, RIGHT or CENTER.
padx can be used to add additional horizontal padding around a text label.
The default padding is 1 pixel. pady is similar for vertical padding.'''
