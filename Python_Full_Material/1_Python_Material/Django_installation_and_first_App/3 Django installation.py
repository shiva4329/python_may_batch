Installing DJango Software:

step 1: first install python software

step 2 :create a folder------>"djangoapps" within c-drive and install django s/w in it.
        don,t install django s/w in same python folder
        so for that create virtual environment , in that install django s/w.
        if even any modifications we do in django, it wont effect python s/w.

        -virtual environment is created for python and in that we install django
        -means in ur system u have 2 python softwares
         i)one in original
         ii)one in virtual environment for Django

step 3: Installing virtual Environment module------->used for creating virtual environment
    
       goto Command prompt:
       goto specified path---->python37/scripts and install vitualenvironment

       C:\Python37\Scripts>pip install virtualenv

       Successfully installed virtualenv-16.7.7
       
------------------------------------------------------------------------------------------------------

step  4: Creating Virtual Environment
         in "djangoapps" folder we create virtual environment
         
         C:\djangoapps>C:\Python37\Scripts\virtualenv myvenv    #here myvenv is name of virtualenvironment]
         
         Installs setuptools, pip, wheel...done.
------------------------------------------------------------------------------------------------------

step 5 : Starting or Activating Virtual environment.
         goto djangoapps/myvenv/scripts and activate it

         C:\djangoapps>cd myvenv

         C:\djangoapps\myvenv>cd Scripts

         C:\djangoapps\myvenv\Scripts>activate

         (myvenv) C:\djangoapps\myvenv\Scripts>
        here we are manually creating virtual environment,
        in Pycharm IDE ,by default , we get virtual environment
-------------------------------------------------------------------------------------------------------
step 6: install Django software using pip in virtual environment

(myvenv) C:\djangoapps\myvenv\Scripts>pip install django  #while installing django virtualenv should be started
                                    (or)pip install django==1.11 (for specific version to be installed)
Successfully installed django-3.0. pytz-2019.3 sqlparse-0.3.0

--------------------------------------------------------------------------------------------------
Step 7: Creating projects in Django
        In django software by default we get Admin module
        in django s/w , we get a server called "django default server"
                        we also get a database called "sqlite"
        Every web application requires server(like tomact) and database
        here we get these , no need to install explicitly

        
(myvenv) C:\djangoapps\myvenv\Scripts>cd\

(myvenv) C:\>cd djangoapps
---------------------------------------------------------------------------
#step 7:
within djangoapps folder, creating the project folder

using django-admin we create project folder

(myvenv) C:\djangoapps>django-admin startproject project1

#here project1 is the projectname
gotoC:/djangoapps/cd project1
C:/djangoapps/project1

here bydefault we see some files in it.
 here we see a file "settings.py" file------->we need to add some code in it

 open settings.py(in IDLE mode) and add the following stmt at the last

STATIC_ROOT=os.path.join(BASE_DIR,'static')

-------------------------------------------------------------------------------------------------------
step 8: migrating the tables etc

(myvenv) C:\djangoapps\project1>python manage.py migrate

#any changes in model class , then you can migrate again
------------------------------------------------------------------------------------------------------
step 9:
(myvenv) C:\djangoapps\project1>python manage.py runserver


Starting development server at http://127.0.0.1:8000/
                                      --------- -----
#here ----->127.0.0.1   is  local host   and 8000 is portno of the server
#for tomcat it is 8080

To check whether server started or not goto browser(chrome)                                      
http://localhost:8000
        (or)
http://127.0.0.1:8000/

#we get----->The install worked successfully! Congratulations!

open browser and type
http://localhost:8000/admin

it asks for username and password  , we need to create them

-----------------------------------------------------------------------------------------------------
step 10: Creating a superuser
#server should be in running state in one window, then only we can create superuser
# open a new comdprompt and start virtual environment
C:\djangoapps\myvenv>cd Scripts

C:\djangoapps\myvenv\Scripts>activate

#creating superuser

(myvenv) C:\djangoapps\myvenv\Scripts>cd\

(myvenv) C:\>cd djangoapps

(myvenv) C:\djangoapps>cd project1
myvenv) C:\djangoapps\project1>python manage.py createsuperuser
Username (leave blank to use 'welcome'): vijay
Email address: vijaysundertrainings@gmail.com

Password: python123
Password (again): python123
Superuser created successfully.

#start server again
(myvenv) C:\djangoapps>python manage.py runserver

#now goto browser and type username and password
http://localhost:8000/admin
        username:digitalnest
        password :vijay1234

        Groups
        user          adduser---------->  username :digitalnest
                                          password :python1234 ----->save

                                          homepage-->we see users------->click we get

                                          username
                                          digitalnest------------->True admin user
                                          vijay                   false

we have logout button----->to logout



