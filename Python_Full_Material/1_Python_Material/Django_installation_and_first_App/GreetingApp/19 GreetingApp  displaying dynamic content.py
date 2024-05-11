
#GreetingApp :Based on the current time , it should wish or great accordingly

#step 1: Open Atom IDE and select djangoapps folder in which virtual environment is installed

#step2 : Activate virtual environment
C:\Users\welcome>cd\

C:\>cd C:\djangoapps\myvenv\Scripts

C:\djangoapps\myvenv\Scripts>activate

(myvenv) C:\djangoapps\myvenv\Scripts>pip install django (if django is not installed)

------------------------------------------------------------------------------------------------------

#step 3: creating and starting project

(myvenv) C:\djangoapps\myvenv\Scripts>cd..

(myvenv) C:\djangoapps\myvenv>cd..

(myvenv) C:\djangoapps>django-admin startproject myproj14

(myvenv) C:\djangoapps>cd myproj14

(myvenv) C:\djangoapps\myproj14>tree /f
Folder PATH listing for volume 64WinXP
Volume serial number is 3AA2-BB2A
C:.
│   manage.py
│
└───myproj14
        settings.py
        urls.py
        wsgi.py
        __init__.py

#-----------------------------------------------------------------------------------------------------
#step 4: Creating and starting Application
(myvenv) C:\djangoapps>cd myproj14

(myvenv) C:\djangoapps\myproj13>python manage.py startapp GreetingApp

#----------------------------------------------------------------------------------------------------
#step 5: open views.py
from django.shortcuts import render
import datetime
# Create your views here.
def input(request):
    dt=datetime.datetime.now()
    time=int(dt.strftime("%H"))
    day_no=dt.strftime("%j")
    msg="Hello.......Hyderabad!!!..."
    if(time<12):
        msg=msg+"Very Good Morning.."
    elif(time<=16):
        msg=msg+"Very Good Afternoon.."
    elif(time<=20):
        msg=msg+"Very Good Evening.."
    else:
        msg=msg+"Very Good Night.."

    dict1={'msg':msg,'dayno':day_no}
    return render(request,'base.html',context=dict1)
#----------------------------------------------------------------------------------------------------
#step 6: Create templates folder
myproj14(outer directory)--->rightclick---->newfolder---->NAME:templates


expand myproj14----->rightclick on templates--->newfile---->Name:base.html----->enter

<html>
<head>
  <style>
    body{
        background:red;
        color:white
       }
    h1{
      color:white
    }
    h2{
      color:yellow
    }
    body{
         background:red
  </head>
  <body>
   <h1>{{msg}} </h1><hr> #{{msg}}   these are tempalte tags and the code is called jinja2 code(seperate scripting language)
                               #IT is not html code or python code.
   <h2>   Current Day No : {{dayno}} </h2>
   </h1>
  </body>
</html>

#------------------------------------------------------------------------------------------------------
#step 7: Adding templates folder to settings .py

TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')



#TEMPLATES = [
#   {
#        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],   #add here

#------------------------------------------------------------------------------------------------------

#step 8: goto application urls.py

Expand myproj13
             -->DateTimeApp---->rightclick---->newfile---> Name:urls.py  
                                                    

                 
 open urls.py of DateTimeApp and write this code

from django.conf.urls import url  

from . import views    
app_name='GreetingApp'
urlpatterns=[
    url(r'^$',views.input,name='input'),
    
]

#-------------------------------------------------------------------------------------------------------
#step 9: Adding applicationurls into project project urls

now open myproj14/urls.py file and add the following
from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from django.conf.urls import url
from GreetingApp import views
urlpatterns = [
path('admin/', admin.site.urls),
url(r'^GreetingApp/',include('GreetingApp.urls'))  #Adding applicationurls into project project urls
]

#-----------------------------------------------------------------------------------------------------
#step 10: migrate

(myvenv) C:\djangoapps\myproj14>python manage.py migrate
--------------------------------------------------------------------------------------------
#step 11 :runserver

(myvenv) C:\djangoapps\myproj14>python manage.py runserver

------------------------------------------------------------------------------------------------------
#step 12: open browser and give request

http://127.0.0.1:8000/GreetingApp/

Ouput:
    Hello.......Hyderabad!!!...Very Good Afternoon..
    Current Day No : 330


-----------------------------------------------------------------------------------------------------

we can also retutn multiple html files  within view function as...

from django.shortcuts import render
import datetime
# Create your views here.
def input(request):
    dt=datetime.datetime.now()
    time=int(dt.strftime("%H"))
    day_no=dt.strftime("%j")
    dict1={'date':dt,'day':day_no}
    if(time<12):
        return render(request,'Morning.html',dict1)
    elif(time<=16):
        return render(request,'Afternoon.html',dict1)
    elif(time<=20):
        return render(request,'Evening.html',dict1)
    else:
        return render(request,'Night.html',dict1)

-----------------------------------------------------------------------------------------------------
#Morning.html
 <html>
<head>
  <style>
    body{
        background:red;
        color:white
       }
    h1{
      color:yellow
    }
    h2{
      color:green
    }
  </style>
  </head>
 <body>
   <h1>Hello.....Good Morning.....</h1>
   <h2>Current date and time is:{{date}} </h2><hr>
       Current Day No : {{day}}
  </body>
</html>
#-----------------------------------------------------------------------------------------------------
#Afternoon.html
 <html>
<head>
  <style>
    body{
        background:red;
        color:white
       }
    h1{
      color:yellow
    }
    h2{
      color:green
    }
  </style>
  </head>
 <body>
   <h1>Hello.....Good Afternoon.....</h1>
   <h2>Current date and time is:{{date}} </h2><hr>
       Current Day No : {{day}}
  </body>
</html>
#----------------------------------------------------------------------------------------------------
#Evening.html
<html>
<head>
  <style>
    body{
        background:red;
        color:white
       }
    h1{
      color:yellow
    }
    h2{
      color:green
    }
  </style>
  </head>
 <body>
   <h1>Hello.....Good Morning.....</h1>
   <h2>Current date and time is:{{date}} </h2><hr>
       Current Day No : {{day}}
  </body>
</html>
#-----------------------------------------------------------------------------------------------------
#Night.html
<html>
<head>
  <style>
    body{
        background:red;
        color:white
       }
    h1{
      color:yellow
    }
    h2{
      color:green
    }
  </style>
  </head>
 <body>
   <h1>Hello.....Good Morning.....</h1>
   <h2>Current date and time is:{{date}} </h2><hr>
       Current Day No : {{day}}
  </body>
</html>

--------------------------------------------------------------------------------------------
#we can also specify multiple url patterns for views.py

now open myproj14/urls.py file and add the following
from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from django.conf.urls import url
from GreetingApp import views
urlpatterns = [
path('admin/', admin.site.urls),
url(r'^www.hello.com$',include('GreetingApp.urls')),
url(r'^$',include('GreetingApp.urls')),
url(r'^hello$',include('GreetingApp.urls')),
url(r'^GreetingApp$',include('GreetingApp.urls'))
]


giving request:4 ways  (any one is fine)
http://127.0.0.1:8000/GreetingApp
       or
http://127.0.0.1:8000/www.hello.com
        or
http://127.0.0.1:8000/hello
        or
http://127.0.0.1:8000/
        


#-----------------------------------------------------------------------------------------------------
Ex:1
goto Application URL
'''
from django.conf.urls import url  

from . import views    
app_name='GreetingApp'
urlpatterns=[
    url(r'^$',views.input,name='input'),    or url(r'^$',views.input) 
]'''

#Commenting Application URL and execute project urls as

from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from django.conf.urls import url
from GreetingApp import views
urlpatterns = [
path('admin/', admin.site.urls),
url(r'GreetingApp/',views.input)
]
----------------------------------------------------------------------------------------------

if i remove admin url-----------> we cant access admin application , as of now we wont see any change





