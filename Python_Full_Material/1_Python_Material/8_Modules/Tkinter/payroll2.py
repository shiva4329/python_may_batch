#Advanced payroll managment system
from tkinter import *
import random,time
payroll=Tk()
payroll.geometry("1350x550+0+0")
payroll.title("Advance payment system")
text_input=StringVar()

#Top frame
Top=Frame(payroll,width=1350,height=50,bg="Red")
Top.pack(side=TOP)

#left frame
Left=Frame(payroll,width=650,height=600)
Left.pack(side=LEFT)

#Right frame
Right=Frame(payroll,width=650,height=600,bg="sky blue")
Right.pack(side=RIGHT)
#---------------------------------------------------------------------------------

info=Label(Top,font=('arial',20,'bold'),text="Advanced Payroll management System",fg="black",anchor='w')
info.grid(row=0,column=0)

#-------------------------------------------------------------------------------
# left sub frames
Left1=Frame(Left,width=650,height=200)
Left1.pack(side=TOP)

Left2=Frame(Left,width=325,height=200)
Left2.pack(side=LEFT)

Left3=Frame(Left,width=325,height=200,bg="pink")
Left3.pack(side=RIGHT)

#-------------------------------------------------------------------------------
# Right sub frames
Right1=Frame(Right,width=650,height=200,bg="yellow")
Right1.pack(side=TOP)

Right2=Frame(Right,width=325,height=200,bg="blue")
Right2.pack(side=LEFT)

Right3=Frame(Right,width=325,height=200,bg="pink")
Right3.pack(side=RIGHT)
#------------------------------------------------------------------------------
# left side Employee name
LeftEmployeeName=Label(Left1,font=('arial',20,'bold'),text="Employee Name :",fg="steel blue",bd=10,anchor='w')
LeftEmployeeName.grid(row=0,column=0)
inputEmployeeName=Entry(Left1,bd=10,width=50,bg="powder blue",justify="right")
inputEmployeeName.grid(row=0,column=1)

LeftEmployeeAdress=Label(Left1,font=('arial',20,'bold'),text="Adress :",fg="steel blue",bd=10,anchor='w')
LeftEmployeeAdress.grid(row=1,column=0)
inputEmployeeAdress=Entry(Left1,bd=10,width=50,bg="powder blue",justify="right")
inputEmployeeAdress.grid(row=1,column=1)

LeftEmployeeMobile=Label(Left2,font=('arial',20,'bold'),text="Mobile :",fg="steel blue",bd=10,anchor='w')
LeftEmployeeMobile.grid(row=0,column=0)
inputEmployeeMobile=Entry(Left2,width=10,bg="white",justify="right")
inputEmployeeMobile.grid(row=0,column=1)

payroll.mainloop()
