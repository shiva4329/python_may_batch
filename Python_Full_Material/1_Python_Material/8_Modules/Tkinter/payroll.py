
#Advanced Payroll Management System

from tkinter import *
import random
import time

payroll=Tk()
#Specifying the size
payroll.geometry("1350x550+0+0")
payroll.title("ADVANCED PAYROLL MANAGEMENT SYSTEMS")

text_Input=StringVar()

#Top Frame
Tops=Frame(payroll,width=1350,height=50,bg="sky blue")
Tops.pack(side=TOP)

#Left Frame
LF=Frame(payroll,width=700,height=650,bg="sky blue")
LF.pack(side=LEFT)

#Right Frame
RF=Frame(payroll,width=600,height=650,bg="sky blue")
RF.pack(side=RIGHT)

lblInfo=Label(Tops,font=('arial',50,'bold'),text="Payroll Management Systems", fg="Steel Blue",bd=10,
               anchor="w") 
lblInfo.grid(row=0,column=0)


LeftInsideLF1=Frame(LF,width=700,height=200)
LeftInsideLF1.pack(side=TOP)

LeftInsideLF2=Frame(LF,width=325,height=400,bg="red")
LeftInsideLF2.pack(side=LEFT)

LeftInsideRF1=Frame(LF,width=325,height=400,bg="black")
LeftInsideRF1.pack(side=RIGHT)
#-----------------------------------------------------------------------------------------
RightInsideLF1=Frame(RF,width=600,height=200)
RightInsideLF1.pack(side=TOP)

RightInsideLF2=Frame(RF,width=300,height=400,bg="red")
RightInsideLF2.pack(side=LEFT)

RightInsideRF1=Frame(RF,width=300,height=400,bg="black")
RightInsideRF1.pack(side=RIGHT)

lblEmployeeName=Label(LeftInsideLF1,font=('arial',12,'bold'),text="Employee Name",fg="Steel Blue",
                       bd=10,anchor="w")
lblEmployeeName.grid(row=0,column=0)
txtEmployeeName=Entry(LeftInsideLF1,bd=10,width=50,bg="powder blue",justify="right")
txtEmployeeName.grid(row=0,column=1)

lblAddress=Label(LeftInsideLF1,font=('arial',12,'bold'),text="Address",fg="Steel Blue",
                       bd=10,anchor="w")
lblAddress.grid(row=1,column=0)
txtAddress=Entry(LeftInsideLF1,bd=10,width=50,bg="powder blue",justify="right")
txtAddress.grid(row=1,column=1)

#-------------------------------------------RightFrame----------------------------------------------
lblPinCode=Label(RightInsideLF1,font=('arial',12,'bold'),text="Pin Code",fg="Steel Blue",
                       bd=10,anchor="w")
lblPinCode.grid(row=0,column=0)
txtPinCode=Entry(RightInsideLF1,bd=10,width=50,bg="powder blue",justify="right")
txtPinCode.grid(row=0,column=1)

lblGender=Label(RightInsideLF1,font=('arial',12,'bold'),text="Gender",fg="Steel Blue",
                       bd=10,anchor="w")
lblGender.grid(row=1,column=0)
txtGender=Entry(RightInsideLF1,bd=10,width=50,bg="powder blue",justify="right")
txtGender.grid(row=1,column=1)

payroll.mainloop()


