


#ADD Application: Accepting 2 values from the user (browser) and performing addition.


#step 1: Open Atom IDE and select djangoapps folder in which virtual environment is installed

#step 1: Activate Virtual Environment

C:\>cd djangoapps1

C:\djangoapps1>cd myvenv

C:\djangoapps1\myvenv>cd Scripts

C:\djangoapps1\myvenv\Scripts>activate

(myvenv) C:\djangoapps1\myvenv\Scripts>
#----------------------------------------------------------------------------------------------------
#Step 2: Creating or starting a project
#we need to create the project within djangoapps1 folder
(myvenv) C:\djangoapps1\myvenv\Scripts>cd..

(myvenv) C:\djangoapps1\myvenv>cd..

(myvenv) C:\djangoapps1>django-admin startproject myproj2

(myvenv) C:\djangoapps1>cd myproj2

(myvenv) C:\djangoapps1\myproj2>tree /f
Folder PATH listing for volume 64WinXP
Volume serial number is 3AA2-BB2A
C:.
│   manage.py
│
└───myproj2
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __init__.py
#----------------------------------------------------------------------------------------------------
#step 3: Creating or starting an Application

(myvenv) C:\djangoapps1\myproj2>python manage.py startapp Addapp

(myvenv) C:\djangoapps1\myproj2>cd Addapp

(myvenv) C:\djangoapps1\myproj2\Addapp>tree /f
Folder PATH listing for volume 64WinXP
Volume serial number is 3AA2-BB2A
C:.
│   admin.py
│   apps.py
│   models.py
│   tests.py
│   views.py
│   __init__.py
│
└───migrations
        __init__.py


(myvenv) C:\djangoapps1\myproj2\Addapp>cd..

(myvenv) C:\djangoapps1\myproj2>

#-----------------------------------------------------------------------------------------------------
#step 4: open views.py within Application folder.
from django.shortcuts import render
from django.http import HttpResponse

def input(request):
    return render(request,"base.html")


def Add(request):
    x=int(request.GET['t1'])   #getting data of textfield t1 and t2
    y=int(request.GET['t2'])
    return HttpResponse(x+y)

#process:

1st request forwarded to ---->input view

input view displays---------->html page(here we enter data and click submit)---req--->

----->data received by Add view ------>gives response and data stored in response object

#----------------------------------------------------------------------------------------------------
#Step 5 : creating Templates folder for including html files within it

#Note: All html files are stored in templates folder , so that all applications views can access
#these html files

myproj2(outer folder)--->rightclick---->newfolder---->NAME:templates


expand myproj2----->rightclick on templates--->newfile---->Name:base.html----->enter
                                                       
<html>
<body bgcolor='yellow' text='blue'>
<form action="./Add" method="get">
Enter First No:<input type="text" name="t1"> <br>
Enter second No:<input type="text" name="t2"><br>
<input type="submit" value="add">
</form>
</body>
</html>
#----------------------------------------------------------------------------------------------------
#step 6: Adding template to settings.py

goto settings.py and type this
#1. To print the filenmae
print(__file__)  #----->displays the filename

(myvenv) C:\djangoapps1\myproj2\myproj2>python settings.py
settings.py         #displays the file name


#2.to know the absolute path where this file(settings.py) is available then
#we have a module called os module
type this in settings.py
 import os
 print(__file__)                     #displays the filename
 print(os.path.abspath(__file__))    #displays the path of the file , where it is


(myvenv) C:\djangoapps1\myproj2\myproj2>python settings.py   #executing settings.py file
settings.py                                                  #displaying filename
C:\djangoapps1\myproj2\myproj2\settings.py                   #displaying the file path



#3. I want directoryname of the file

print(os.path.dirname(os.path.abspath(__file__)))

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

#Executing settings.py
(myvenv) C:\djangoapps\myproj2\myproj2>python settings.py
C:\djangoapps\myproj2\myproj2  #directory name
C:\djangoapps\myproj2\myproj2


#4.
Ex: I have C:\djangoapps\myproj2\templates
     I want to print this location
     
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR) ----> this printsC:\djangoapps\myproj2

(myvenv) C:\djangoapps\myproj2\myproj2>python settings.py
C:\djangoapps\myproj2

In BASE_DIR ------->i have templates folder

i want to refer this templates folder

include this line in settings.py after BASE_DIR

TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')
                   means to the BASE_DIR add templates folder also
print(TEMPLATE_DIR)


o/p:
(myvenv) C:\djangoapps\myproj9\myproj9>python settings.py
C:\djangoapps\myproj9\templates


Now adding this TEMPLATE_DIR into templates

#-----------------------------------------------------------------------------------------------------
#step 6: open settings.py and add this

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(BASE_DIR)
TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')
print(TEMPLATE_DIR)

include this TEMPLATE_DIR in templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],  #add here

#-----------------------------------------------------------------------------------------------------
#STEP 7: open urls.py file in inner project directory

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Addapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^Addapp$',views.input'),
    url(r'^Add$',views.Add)
]

-----------------------------------------------------------------------------------------------------
#step 8: migrate

(myvenv) C:\djangoapps\myproj2\myproj2>cd..

(myvenv) C:\djangoapps\myproj2>python manage.py migrate

------------------------------------------------------------------------------------------------------
#step 11 : startserver

(myvenv) C:\djangoapps\myproj2>python manage.py runserver

-----------------------------------------------------------------------------------------------------
#step 12 : Goto Browser and give request
http://127.0.0.1:8000/Addapp/

Enter 1st No:10
Enter 2nd No:20
        ADD------------>30

ctrl+c----------->to stop the server
----------------------------------------------------------------------------------------------------












        
