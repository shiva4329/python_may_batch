#working with models and databases:

-without database there is no real-time application.

-we generally retrieve data from databases.

-django has simplified the database communication with python.

-django itself provides a in-built or default database called "sqlite3"

-for small to medium scale applications we can go with "sqlite3"

-for heavy database applications , we can go with oracle or mysql databases;


#Database Configurations:
if we want to use default database "sqlite3" then no need of any configurations

but to set any other database then goto settings.py file and configure

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#here by default the database is set to sqlite3, here no need of any configuration


for ur web Application whether database support is there or not ..check it once...

check whether database is properly configured or not , for that...

goto cmdprompt----->
#step 1:
C:\djangoapps\myvenv\Scripts>activate

(myvenv) C:\djangoapps\myvenv\Scripts>cd..

(myvenv) C:\djangoapps\myvenv>cd..

(myvenv) C:\djangoapps>cd myproj16

#step2 :check whether database is properly configured or not , for that... execute the following 3 commands


(myvenv) C:\djangoapps\myproj16>py manage.py shell #opening django shell

we get this( interactive mode)
    
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
#---------------------------------------------------------------------------------------------------
#ii)
>>> from django.db import connection
>>>

you should not get any error---->means here connection object is created

-next create cursor object------>for executing any valid sql query
#---------------------------------------------------------------------------------------------------
#iii)
>>> cur1=connection.cursor()   #cursor object created
>>>

now we can say that for our application database is properly configured

>>>exit()
#---------------------------------------------------------------------------------------------------
If we want to create a database table,
we no need to write single line of code realted to sql query in django , we write in python only...

for that we have model class.

we have models.py file------->to define model classes

each model class refers one database table

define a model class and use a small command so that the model class  can be
converted to a database table.

A model is a python class which contains the database information.

A database table consists of columns like eid,ename,sal,sex,dno,city...

these columns we need to specify in model class.

#how to define a model class>

-inside models.py

#----------------------------------------------------------------------------------------------------
#create a ModelApp

#step 3: creating and starting project

(myvenv) C:\djangoapps>django-admin startproject myproj17

(myvenv) C:\djangoapps>cd myproj17

#--------------------------------------------------------------------------------------------------
#step 4: Creating and starting Application

(myvenv) C:\djangoapps\myproj17>python manage.py startapp ModelApp

(myvenv) C:\djangoapps\myproj17>

#--------------------------------------------------------------------------------------------------
#step 5: goto models.py in Application folder(ModelApp).

from django.db import models

# Create your models here.
class Emp(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=20) #---------makemigrations----> sqlcode generates-----execute
    sal=models.FloatField()               #saying "migrate"---------->Table gets created
    sex=models.CharField(max_length=5)
    dno=models.IntegerField()


#here Emp will be ur tablename
#i.e Table name ------->ModelApp.Emp
#    column names------>eno,ename,sal,sex,dno

this model class code to be converted to sqlcode by saying "makemigrations"------>sqlcode generates

if u execute this sql code by saying "migrate"---------->Table gets generated in "migrations" folder
within the Application folder

#----------------------------------------------------------------------------------------------------
#step 5: add ur application in settings.py ------>installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ModelApp'    #addhere
]

#----------------------------------------------------------------------------------------------------
#step 6: makemigrations

(myvenv) C:\djangoapps\myproj17>py manage.py makemigrations #here pythoncode converted to sql code
Migrations for 'ModelApp':
  ModelApp\migrations\0001_initial.py                      #sqlgenerated code 
    - Create model Emp


#sql generated code, we can see within a python file with
#default name under----> migrations\0001_initial.py

#----------------------------------------------------------------------------------------------------
#step 7: goto migrations folder within Application folder(ModelApp)--->we see-->0001_initial.py

open the file we see the following

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=20)),
                ('sal', models.FloatField()),
                ('sex', models.CharField(max_length=5)),
                ('dno', models.IntegerField()),
            ],
        ),
    ]


#Note : here along with the columns(5) that we specified we get a new column(id) which is generated
#automatically and is taken as primary key column with auto increment of values like 1,2,3,4,5

#----------------------------------------------------------------------------------------------------
#step 8: to see the equivalent sql code for this pythonfile(0001_initial.py) then

(myvenv) C:\djangoapps\myproj17>py manage.py sqlmigrate ModelApp 0001_initial

#we get this
BEGIN;
--
-- Create model Emp
--
CREATE TABLE "ModelApp_emp" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "eno" integer NOT NULL,
"ename" varchar(20) NOT NULL, "sal" real NOT NULL, "sex" varchar(5) NOT NULL, "dno" integer NOT NULL);
COMMIT;

#-----------------------------------------------------------------------------------------------------
#step 9: migrate
executing the sqlcode to generate sql table

(myvenv) C:\djangoapps\myproj17>py manage.py migrate


Operations to perform:
  Apply all migrations: ModelApp, admin, auth, contenttypes, sessions
Running migrations:
  Applying ModelApp.0001_initial... OK
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK

#here not only the sql table is generated ,many other tables are generated when we say --->migrate
#here by default we have many in-built applications within this django
#we can see them in the-------> installed apps of settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',  #in-built applications
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ModelApp'
]

#above--->when we say migrate-->migrations applied on all these in-built applications
#--------------------------------------------------------------------------------------------    
#step 10: admin Module
#where we see this------>i)in installed apps of settings.py
                        ii)in urls.py, we see admin url
                        iii)in Application folder(ModelApp) we see admin.py


#How to launch admin interface:
    In admin interface, we can see our created table and also perfom CRUD operations
    C-Create
    R-Read
    U-Update
    D-Delete

#-------------------------------------------------------------------------------------------------
#Step 11: runserver
(myvenv) C:\djangoapps\myproj17>py manage.py runserver

#---------------------------------------------------------------------------------------------------
#step 12: goto browser and open admin interface by giving the following request

http://127.0.0.1:8000/admin

It asks for username and password:

#---------------------------------------------------------------------------------------------------
#step 13: create superuser

#stop server------>ctrl+c

(myvenv) C:\djangoapps\myproj17>py manage.py createsuperuser
Username (leave blank to use 'dell'): vijay
Email address: vijaysundertrainings@gmail.com
Password: python123
Password (again): python123
Superuser created successfully.

#---------------------------------------------------------------------------------------------------
#start server
(myvenv) C:\djangoapps\myproj17>py manage.py runserver

#step 14: goto browser and open admin interface by giving the following request

http://127.0.0.1:8000/admin
username: vijay
passwoird : python123

django admin console opens-------->but table is not seen---->for that register model to admin interface

#-----------------------------------------------------------------------------------------------------
#step 15: register model to admin interface
goto admin.py in Application folder(ModelApp) and write this

from ModelApp.models import Emp
admin.site.register(Emp)

#----------------------------------------------------------------------------------------------------
#step 16: refresh the browser

we can see the table----->Emps



MODELAPP
Emps	Add   Change

#-----------------------------------------------------------------------------------------------------



