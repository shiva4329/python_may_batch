


without model class we cannot communicate with database.
here we are not writing sql queries , here we perform CRUD operations using model class only
from model class------->creating table

similarly if table already available---->we can generate model class from it.


to see ur sql table---->we need to register our model class to admin interface in admin.py
#admin.py'
from django.conf  import admin
from DemoApp.models import Emp
admin.site.register(Emp)   #here Emp is the modelclass getting registered with admin site

#----------------------------------------------------------------------------------------------
opening admin interface:
    -using superuser and password

py manage.py create superuser

provide username,emailid,password.

http://127.0.0.1:8000/admin

here always should use admin as the url pattern only
bcoz admin is a built-in appplication where its url pattern is specified in urls.py file
if changed in urls.py file ,her also we can change


-----------------------------------------------------------------------------------------------------
add 5 emp records----->save and addanother



Eno:
105
Ename:
James
Sal:
50000
Sex:
m
Dno:
11
   ------>save

employee details wont be dispalyed---------->employeeobject will be displayed as

        EMP
	Emp object (5)
	Emp object (4)
	Emp object (3)
	Emp object (2)
	Emp object (1)

so to get empdata

 goto models.py and write

class Emp(models.Model):
    eno=Model.IntegerField()
    ename=Model.CharField(max_length=20)
    sal=Model.FloatField()              
    sex=Model.CharField(max_length=5)
    dno=Model.IntegerField()

    def __str__(self):   #add this
        return self.ename

now refresh browser we get ename for all emp objects

----------------------------------------------------------------------------------------------------
not only ename, i want all columns of table to be displayed

for that define ModelAdmin(MA) class  in admin.py

from ModelApp.models import Emp

class EmpAdmin(admin.ModelAdmin):#follow the naming convention--->EmpAdmin where Emp is model class
    list_display=['eno','ename','sal','sex','dno']   #list_display is pre-defined
admin.site.register(Emp,EmpAdmin)   #register EmpAdmin also

#this modelAdmin class will decide in admin interface, how this model information to be displayed

#refresh browser-------->we see all fields

we can modify and delete the fields by dblclicking  on eno and modify and delete

for sorting based on ename-------->click on "ename"----->by default it gets sorted
                                   even for the other fields also


    

To display 'id' field also specify as

  list_display=['id','eno','ename','sal','sex','dno']

 when we are displaying all columns then------>__str__()method is not required

 Action--->delete selected employees
           select and delete

so here no need to write any sql queries

we have may datatypes--->like date ,email etc --->to see all those

goto documentation------->goto djangoproject.com------->search : models------->models and databases

goto model field reference----->to see all datattypes

-----------------------------------------------------------------------------------------------
Now displaying the data present in the database to the enduser

#step:   open views.py and write the following
from django.shortcuts import render
from ModelApp.models import Emp
# Create your views here.
def emp_input(request):
    emps=Emp.objects.all()
    return render(request,'base.html',{'emps':emps})

------------------------------------------------------------------------------
#Step : create base.html under templates

myproj17------>rightclick------>newfolder--->templates
--->right click------>base.html

<html>
  <head>

  </head>
  <body>
    <h1> Employees information </h1>
     {% if emps % }
        <table border=4>
           <thead>
             <th>EMP NO</th>
             <th>EMP NAME</th>
             <th>SALARY </th>
             <th>SEX </th>
             <th>DNO </th>
           </thead>
      {% for p in emps  %}
       <tr>
         <td>{{p.eno}}</td>
         <td>{{p.ename}}</td>
         <td>{{p.sal}}</td>
         <td>{{p.sex}}</td>
         <td>{{p.dno}}</td>
       </tr>
       {%endfor%}
      </table>
      {%else%}
         <p> No Employee records are found!!!</p>
      {%endif%}
  </body>
</html>

#-------------------------------------------------------------------------------
#step: open urls.py

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from ModelApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.emp_input)
]
#-------------------------------------------------------------------------------
#step : goto settings.py


TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')



#TEMPLATES = [
#   {
#        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],   #add here

#-------------------------------------------------------------------------------







































ex:JobApp(joining date,location,offered salary,qualification)
   BookApp(title,author,published year,price)
   CustomerApp(cid,cname,Accno,bank,bal,Address)
  










