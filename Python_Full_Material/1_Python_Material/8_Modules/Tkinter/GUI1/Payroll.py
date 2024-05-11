from tkinter import *
import random,time
payroll=Tk()
payroll.geometry("1250x550+0+0")
payroll.title("Adavnced Payroll Management Systems")
text_Input=StringVar()

#Top frame
Tops=Frame(payroll,width=1350,height=50,bg="skyblue").pack(side=TOP)
info=Label(Tops,font=('arial',25,'bold'),text="Advanced Payroll management system",fg='yellow',bd=10,anchor='w').pack()
#Left frame
Left=Frame(payroll,width=700,height=650,bg="red").pack(side=LEFT)
Left1=Frame(Left,width=250,height=200).pack(side=TOP)
Left2=Frame(Left,width=250,height=200,bg="black").pack(side=LEFT)
Left3=Frame(Left,width=200,height=200,bg="pink").pack(side=RIGHT)
#Right frame
Right=Frame(payroll,width=700,height=650,bg="green").pack(side=RIGHT)
Right1=Frame(Right,width=200,height=200).pack(side=TOP)
Right2=Frame(Right,width=200,height=200,bg="red").pack(side=LEFT)
Right3=Frame(Right,width=200,height=200,bg="white").pack(side=RIGHT)
info=Label(Tops,font=('arial',25,'bold'),text="Advanced Payroll management system",fg='yellow',bd=10,anchor='w')
#info.grid(row=0,column=0)




payroll.mainloop()