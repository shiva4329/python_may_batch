#Creating our first application

#WelcomeApp

#step 1: Activate virtual environment.
C:\>cd djangoapps1

C:\djangoapps1>cd myvenv

C:\djangoapps1\myvenv>cd Scripts

C:\djangoapps1\myvenv\Scripts>activate

(myvenv) C:\djangoapps1\myvenv\Scripts>

#step 2:starting/creating a project

(myvenv) C:\djangoapps1>django-admin startproject myproj1
#---------------------------------------------------------------------------------------------------
#step 3: to check whether the project structure is crearted or not 
(myvenv) C:\djangoapps1>cd myproj1

(myvenv) C:\djangoapps1\myproj1>tree /f
Folder PATH listing for volume 64WinXP
Volume serial number is 3AA2-BB2A
C:.
│   manage.py
│
└───myproj1
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __init__.py
#---------------------------------------------------------------------------------------------------
#step 4: starting/creating Application
(myvenv) C:\djangoapps1\myproj1>python manage.py startapp WelocmeApp

(myvenv) C:\djangoapps1\myproj1\WelocmeApp>tree /f
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
#------------------------------------------------------------------------------------------------
#Step 5: goto settings.py and add the following stmt at the last
import os
STATIC_ROOT=os.path.join(BASE_DIR,'static')

-------------------------------------------------------------------------------------------------------
#Step 6: goto views.py ----->write the following code

from django.shortcuts import render
from django.http import HttpResponse
def display(request):
    return HttpResponse("<html><body bgcolor='yellow' text='red'><h1>Welcome...to Django!!!</h1></body></html>")

-------------------------------------------------------------------------------------------------------
#step 7: goto urls.py file in myproj2------->write the following code
from django.contrib import admin
from django.urls import path
#from django.conf.urls import url
from django.urls import re_path as url # ----> added in 2023 by siva
from WelcomeApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^WelcomeApp$',views.display),
    url(r'^hello$',views.display),
    url(r'^$',views.display),
]
#---------------------------------------------------------------------------------------------------------
#step 7.1: goto settings.py file in myproj2------->write the following code
INSTALLED_APPS = [
    'django.contrib.admin', # --> add this line
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Welcome_App_main.apps.WelcomeAppMainConfig',
]
#----------------------------------------------------------------------------------------------------
#step 8: 
(myvenv) C:\djangoapps\myproj2>python manage.py migrate

----------------------------------------------------------------------------------------------------
#step 9: start the server

(myvenv) C:\djangoapps\myproj2>python manage.py runserver

#Starting development server at http://127.0.0.1:8000/

---------------------------------------------------------------------------------------------------
#step 10 : Giving request in the browser

http://127.0.0.1:8000/WelcomeApp

o/p: Welcome.....to Django!!!

--------------------------------------------------------------------------------

