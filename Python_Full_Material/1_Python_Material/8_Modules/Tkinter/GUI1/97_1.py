from tkinter import *
master=Tk()
class per:
    def __init__(self):
        frame=Frame(master).pack()
        self.button=Button(master,text="QUIT",fg="red",command=quit).pack(side="left")
        self.button=Button(master,text="RUN",fg="green",command=self.run).pack()
    def run(self):
            Total = int(input("Total Income Amount :"))
            # y=int(input("y:"))
            total = (25 / 100) * Total
            print("My Share =",Total-total," is ",((Total-total)/Total)*100,"%  of Total Income")
            print(" valli Share (25%)= Rs.", total)

APP=per()
master.mainloop()
