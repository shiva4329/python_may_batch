#program illustrating non-static variable(NSV)
class emp:
    company="Infosys"        #SV
    def getdetails(self):
        self.ename=input("Enter employee name:") #NSV's
        self.eid=int(input("Enter empid:"))
        self.esal=int(input("Enter empsal:"))
        self.desig=input("Enter designation:")
        
    def putdetails(self):
        print("Ename:",self.ename) 
        print("Eid:",self.eid)
        print("Esal:",self.esal)
        print("Designation:",self.desig)
        print("Company:",emp.company)
e1=emp()
print(e1)
e1.getdetails()
e1.putdetails() 
#emp().getdetails()  #one more object creates


e2=emp()
e2.getdetails()
e2.putdetails()
    
print(e1.ename)
print(e2.ename)
e1.esal=55000
e1.putdetails()

