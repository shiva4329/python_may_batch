


#Working with Static files within templates:

static files------>css files,javascript files,images,videos etc

previously within template file we used

{{msg}} template tags----->which represents some text

bu now we use some advanced template tag which can perform some processing also

this template tag represented as {%   %} ---->jinja2 template tag language
                                              IT is a seperate template language

To work with static files------>create a folder 'static' just like templates
within 'static' folder create one more folder------->'images'

next add static folder path to settings.py file

within static folder, create 3 folders
1.images ------>for storing mages
2.css --------->for storing CSS file
3.videos------->for storing the videos.

#------------------------------------------------------------------------------------------------------


#StaticApp :

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

(myvenv) C:\djangoapps>django-admin startproject myproj15

(myvenv) C:\djangoapps>cd myproj15

(myvenv) C:\djangoapps\myproj15>tree /f
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

#--------------------------------------------------------------------------------------------------
#step 4: Creating and starting Application

(myvenv) C:\djangoapps>cd myproj15

(myvenv) C:\djangoapps\myproj15>python manage.py startapp StaticApp

(myvenv) C:\djangoapps\myproj15>

#---------------------------------------------------------------------------------------------------
#step 5: open views.py
from django.shortcuts import render
import datetime
# Create your views here.
def input(request):
    dt=datetime.datetime.now()
    time=int(dt.strftime("%H"))
    msg="Hello.......Hyderabad!!!..."
    if(time<12):
        msg=msg+"Very Good Morning.."
    elif(time<=16):
        msg=msg+"Very Good Afternoon.."
    elif(time<=20):
        msg=msg+"Very Good Evening.."
    else:
        msg=msg+"Very Good Night.."

    dict1={'msg':msg,'date':dt}
    return render(request,'base.html',context=dict1)
#-----------------------------------------------------------------------------------------------------
#step 6: Create templates folder
myproj15(outer directory)--->rightclick---->newfolder---->NAME:templates


expand myproj15----->rightclick on templates--->newfile---->Name:base.html----->enter

 <html>
  <body>
   <h1>{{msg}} </h1><hr> #{{msg}}   these are tempalte tags and the code is called jinja2 code(seperate scripting language)
                               #IT is not html code or python code.
   <h2> Current Date and Time: {{date}} </h2>
  </body>
</html>
#----------------------------------------------------------------------------------------------------
#step 7: Adding templates folder to settings .py

TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')



#TEMPLATES = [
#   {
#        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],   #add here

#---------------------------------------------------------------------------------------------------
#Step 8: Create static folder within project outer directory
myproj15(outer directory)--->rightclick---->newfolder---->NAME:static


expand myproj15----->rightclick on static--->newfolder---->Name:images

now copy ur image in C:/djangoapps/myproj15/static/images-------->paste ur image here
#--------------------------------------------------------------------------------------------------
#step 9: goto settings.py and add static folder
now open settings.py and add the path of static folder within it


STATIC_DIR=os.path.join(BASE_DIR,'static')

and goto static line code and add add the following

STATICFILES_DIRS=[STATIC_DIR]  #Here we need to use the same name STATICFILES_DIRS

---------------------------------------------------------------------------------------------------
#step 10: open base.html and include advanced Template tags within it 
{%load staticfiles%}
<html>
 <body>
    <center>
    <h1> {{msg}} </h1>
    <h2> Current DAte and Time : {{date}} </h2>
    <img src="{%static  'images/charminar.jpg'%}"> #already we have set path upto static within settings.py,
                                                   #so just specify the remaining part
    </center>
</body>
</html>

#--------------------------------------------------------------------------------------------------
#step 11: goto project urls.py file and include the following

from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from django.conf.urls import url
from StaticApp import views
urlpatterns = [
path('admin/', admin.site.urls),
url(r'StaticApp/',views.input)
]

#--------------------------------------------------------------------------------------------------
#step 12: migrate

(myvenv) C:\djangoapps\myproj15>python manage.py migrate
--------------------------------------------------------------------------------------------
#step 13 :runserver

(myvenv) C:\djangoapps\myproj15>python manage.py runserver

------------------------------------------------------------------------------------------------------
#step 14: open browser and give request

http://127.0.0.1:8000/StaticApp




OUTPUT:
    Hello.......Hyderabad!!!...Very Good Afternoon..
Current DAte and Time : Nov. 29, 2019, 1:03 p.m.

    charminar pic..........

#-----------------------------------------------------------------------------------------------------
#Step 15: including CSS files within static folder

expand myproj15----->rightclick on static--->newfolder---->Name:css

css-------->rightclick------>newfile------>name:sample1.css

and include the following

body{
    background: red ;
    color:yellow
}

#-----------------------------------------------------------------------------------------------------
#step 16: Include this CSS file and folder within base.html,

open base.html and write this

<head>
  <link rel="stylesheet" href="{%static 'css/sample1.css'%}">
  </head>

#----------------------------------------------------------------------------------------------
#base.html
{%load static%}
<html>
<head>
  <link rel="stylesheet" href="{%static 'css/sample1.css'%}">
  </head>
 <body>
    <center>
    <h1> {{msg}} </h1>
    <h2> Current DAte and Time : {{date}} </h2>
    <img src="{%static  'images/charminar.jpg'%}">
    </center>
</body>
</html>

#-----------------------------------------------------------------------------------------------
#step 17: refresh browser

OUTPUT:

#-------------------------------------------------------------------------------------------------


#Working more on CSS:

#ex:1 :  for Background and text color

body{
    background: red ;
    color:yellow
}

#-------------------------------------------------------------------------------------------------
#ex:2 :
body{
    background: red ;
    color:yellow;
    text-align:center
}
#--------------------------------------------------------------------------------------------------
#ex:3: image border
body{
    background: red ;
    color:yellow;
    text-align:center
}

img{
    border:10px solid green    #border can be------>solid/dotted/groove
   }

#--------------------------------------------------------------------------------------------------
#ex:4

body{
    background: red ;
    color:yellow;
    text-align:center
}

img{
    border:10px dotted green
   }

#--------------------------------------------------------------------------------------------------

#ex:5  for multiple images  goto base.html and repeat the img tag
#base.html
{%load staticfiles%}
<html>
<head>
  <link rel="stylesheet" href="{%static 'css/sample1.css'%}">
  </head>
 <body>
    <center>
    <h1> {{msg}} </h1>
    <h2> Current DAte and Time : {{date}} </h2>
    <img src="{%static  'images/charminar.jpg'%}">
    <img src="{%static  'images/charminar.jpg'%}">
    <img src="{%static  'images/charminar.jpg'%}">
    </center>
</body>
</html>

#---------------------------------------------------------------------------------------------------
#ex:6 for images to be displayed side by side------>set width and height in CSS file

body{
    background: red ;
    color:yellow;
    text-align:center
}

img{
    border:10px solid green
    width:25%;
    height:200px;
   }

#---------------------------------------------------------------------------------------------------
#ex:7 9 images of same pic
#base.html
{%load staticfiles%}
<html>
<head>
  <link rel="stylesheet" href="{%static 'css/sample1.css'%}">
  </head>
 <body>
    <center>
    <h1> {{msg}} </h1>
    <h2> Current DAte and Time : {{date}} </h2>
    <img src="{%static  'images/charminar.jpg'%}">
    <img src="{%static  'images/charminar.jpg'%}">
    <img src="{%static  'images/charminar.jpg'%}">
    <img src="{%static  'images/charminar.jpg'%}">
    <img src="{%static  'images/charminar.jpg'%}">
    <img src="{%static  'images/charminar.jpg'%}">
    <img src="{%static  'images/charminar.jpg'%}">
    <img src="{%static  'images/charminar.jpg'%}">
    <img src="{%static  'images/charminar.jpg'%}">
    </center>
</body>
</html>
#------------------------------------------------------------------------------------------------------




