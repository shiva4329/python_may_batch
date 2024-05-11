# Design a Registration form to student for A Competetive Xam

from tkinter import *
page=Tk()
page.geometry("1080x720+0+0")
x="registration"
page.title(x.capitalize())
#Top frame
Top=Frame(page,width=500,height=20,bg="RED")
Top.pack(side=TOP)
#Top title
TitleName=Label(Top,font=("Times new roman",20,"bold"),text=x.upper(),fg="maroon")
TitleName.pack(side=TOP)
#Left Frame
Left=Frame(page,width=100,height=800)
Left.pack(side=LEFT)
# left side Registration detail
FullName=Label(Left,font=("Times new roman",15,"bold"),text="Full Name : ")
FullName.grid(row=0,column=0)
TextField=Entry(Left,bd=2)
TextField.grid(row=0,column=1)

Address=Label(Left,font=("Times new roman",15,"bold"),text="Address : ")
Address.grid(row=1,column=0)
TextField=Entry(Left,bd=2,width=30)
TextField.grid(row=1,column=1)

Gender=Label(Left,font=("Times new roman",15,"bold"),text="Gender : ")
Gender.grid(row=2,column=0)
TextField=Radiobutton(Left,text="Male",value=1)
TextField.grid(row=2,column=1)
TextField=Radiobutton(Left,text="Female",value=2)
TextField.grid(row=3,column=1)

Mobile=Label(Left,font=("Times new roman",15,"bold"),text="Mobile : ")
Mobile.grid(row=4,column=0)
TextField=Entry(Left,bd=2,width=30)
TextField.grid(row=4,column=1)

HigherGraduation=Label(Left,font=("Times new roman",15,"bold"),text="Higher Degree : ")
HigherGraduation.grid(row=5,column=0)
TextField=Radiobutton(Left,text="M.Tech",value=1)
TextField.grid(row=5,column=1)
TextField=Radiobutton(Left,text="B.Tech",value=2)
TextField.grid(row=6,column=1)

HigherGraduationHallticketNumber=Label(Left,font=("Times new roman",15,"bold"),text="Higher Degree Hallticket Number : ")
HigherGraduationHallticketNumber.grid(row=7,column=0)
TextField=Entry(Left,bd=2,width=30)
TextField.grid(row=7,column=1)

def SUBMIT():
    print("\n ----Registerd Succesfully----- \n")

Submit=Button(Left,text="SUBMIT",command=SUBMIT,justify="center")
Submit.grid(row=10,column=3)


page.mainloop()
