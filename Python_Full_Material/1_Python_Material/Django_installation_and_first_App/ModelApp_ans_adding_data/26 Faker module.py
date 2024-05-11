

#Faker module: To genertate fake data, for Testing purpose

#installing faker module:

c:>pip install faker

C:\djangoapps\myvenv\Scripts>activate

(myvenv) C:\djangoapps\myvenv\Scripts>cd..

(myvenv) C:\djangoapps\myvenv>cd..

(myvenv) C:\djangoapps>cd myproj17

(myvenv) C:\djangoapps\myproj17>pip install faker
-----------------------------------------------------------------------------------------------------
now create a file in C:\djangoapps\fake.py  and write the following

from faker import Faker #here Faker is the class
fake=Faker() #creating object of Faker class

print("Employee Name:",fake.name())  #generates a random nmae(fake name)


(myvenv) C:\djangoapps\myproj17>cd..

(myvenv) C:\djangoapps>py fake.py
Employee Name: James Garcia

(myvenv) C:\djangoapps>py fake.py
Employee Name: Daniel King
#----------------------------------------------------------------------------------------------------
#similarly we can generaate many other random details suchas 
from faker import Faker #here Faker is the class
fake=Faker() #creating object of Faker class

print("Employee Name:",fake.name())
print("Employee First Name:",fake.first_name())
print("Employee Last Name:",fake.last_name())
print("Employee DOB :",fake.date())  #generates random date
print("Employee Email ID:",fake.email()) #generates random email
print("Employee ID:",fake.random_number(5)) #generates random number of length 5
print("Employee sal:",fake.random_int(min=10000,max=99999))
print("Employee Designation/Role:",fake.random_element(elements=('Software Engineer','Team Lead',
'Project Lead','Project Manager')))
print("Employee Address:",fake.address())
print("Employee city :",fake.city())


(myvenv) C:\djangoapps>py fake.py
Employee Name: Ronald Wilson
Employee First Name: Tony
Employee Last Name: Greene
Employee DOB : 2018-08-18
Employee Email ID: rgonzalez@baker.info
Employee ID: 71754
Employee sal: 77939
Employee Designation/Role: Software Engineer
Employee Address: PSC 1142, Box 7315
APO AA 79345
Employee city : North Ronaldside

#----------------------------------------------------------------------------------------------------
#generating 30 random employee records
from faker import Faker 
fake=Faker()

for p in range(30):
      print("Employee Name:",fake.name())
      print("Employee First Name:",fake.first_name())
      print("Employee Last Name:",fake.last_name())
      print("Employee DOB :",fake.date())  #generates random date
      print("Employee Email ID:",fake.email()) #generates random email
      print("Employee ID:",fake.random_number(5)) #generates random number of length 5
      print("Employee sal:",fake.random_int(min=10000,max=99999))
      print("Employee Designation/Role:",fake.random_element(elements=('Software Engineer','Team Lead',
      'Project Lead','Project Manager')))
      print("Employee Address:",fake.address())
      print("Employee city :",fake.city())
      print()
(myvenv) C:\djangoapps>py fake.py
#-----------------------------------------------------------------------------------------------------
#linking fake data dtails to django

myproj17------>rightclick------->populate.py  and writ e the following

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myproj17.settings')
import django
django.setup()

from ModelApp.models import *
from faker import Faker
fake=Faker()
from random import *

def populate(n):
    for i in range(n):
        feno=randint(101,1000)  #randint is a function of random module
        fename=fake.name()
        fesal=randint(10000,70000)
        fsex=fake.random_element(elements=('m','f'))
        fdno=randint(11,14)
        emp_record=Emp.objects.get_or_create(eno=feno,ename=fename,sal=fesal,sex=fsex,dno=fdno)
populate(30)

#-----------------------------------------------------------------------------------------------------
(myvenv) C:\djangoapps\myproj17>py populate.py  #here 30 records added to database

(myvenv) C:\djangoapps\myproj17>py manage.py runserver

first check in admin interface------>30 records will be added
http://127.0.0.1:8000/admin

next check the response
http://127.0.0.1:8000 --------->30 records will be added

again execute
(myvenv) C:\djangoapps\myproj17>py populate.py
agaain 30 records will be added..
