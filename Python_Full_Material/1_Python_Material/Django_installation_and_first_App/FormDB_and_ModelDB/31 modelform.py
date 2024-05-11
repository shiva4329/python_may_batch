

#Model Forms: whenever we define normal forms(forms class),
              Programmer has to define the form fields explicitly with the corresponding datatypes.

           - whenever we are working with normal forms, we recieve the data from the request object,
           store into the form class object and we can perform the validations on the form class object
            by calling is_valid() method.

            -Directly we cannot able to store normal form object data into the database table.
           -In-order to store the normal form object data into the database table , first we read
            the data from the form object, store the data into the model class object and we
             save the model class object data to database.

            - to overcome obove problems, instead of defining normal forms we defime
              model forms.
            -within the model form,instead of defining the formfields expicitly,
             we take the model class attributes.
            -whenever we use modelform object into the template ,dynamically html code will
             be generated within the modelform represenrted model attributes


             Automatically HTML code is generated in 2ways
             1)using forms----->here we specify the columns,their datatypes and sizes,
             2)using modelforms---->here no need to specify the datatpes or sizes

             -Inorder to store the data into the database table after processing the
              validations on the modelform object, directly save modelform object data
              into database table.
             
#here we perform changes in forms.py and views.py only 


#Step 1: open models.py file and type the following

from __future__ import unicode_literals
from django.db import models
class Product(models.Model):
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=20)
    pcost=models.DecimalField(max_digits=10,decimal_places=4)
    pmfd=models.DateField()
    pexpdt=models.DateField()
#-----------------------------------------------------------------------------------------------------
#Step 2: create forms.py file in formDBApp and write the following
# creating forms.py
#       ->rightclick----->FormApp------>create new python file------>Name: forms.py
#previously this was the code for form class
'''from django import forms

class ProductForm(forms.Form):
    pid=forms.IntegerField(label="Enter the pid")
    pname=forms.CharField(label="Enter the ProductName:",max_length=100)
    pcost=forms.DecimalField(label="Enter the pCost",max_digits=100,decimal_places=9)
    pmfd=forms.DateField(label="Enter the mfd:")
    pexpdt=forms.DateField(label="Enter the Expdt:")  '''

#now instead write this modelform class , where datatypes and sizes are not required
from django import forms
from .models import Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['pid', 'pname','pcost','pmfd','pexpdt']
#---------------------------------------------------------------------------------------------------
#modifying views.py
#Step 3: Views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
# Create your views here.

def input(request):
    if(request.method=='POST'):
        form=ProductForm(request.POST)#from the req object we read data and store it in form class object 
        if(form.is_valid()):         # 
            '''
            p=Product(pid=form.cleaned_data['pid'], #now storing the data of form class object into model class object(p)
                      pname=form.cleaned_data['pname'], #and wesave the model class object(p) data to database by saying p.save()
                      pcost=form.cleaned_data['pcost'],
                      pmfd=form.cleaned_data['pmfd'],
                      pexpdt=form.cleaned_data['pexpdt'])
            p.save()
            '''
            form.save()   #directly saving model form object into the database
            return HttpResponse('Product inserted successfully')



    else:
        form=ProductForm()
    return render(request, 'base.html', {'form': form})
#-----------------------------------------------------------------------------------------------------
#step 4: base.html
html>
<body bgcolor="green">
<form action="" method="post">
    {% csrf_token %}
    {{ form }}
    <br>
    <input type="submit" value="Submit" />
</form>
</body>
</html>

#----------------------------------------------------------------------------------------------------
#step 5: urls.py file

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from FormDBApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.input)
]

#----------------------------------------------------------------------------------------------

#Step 6: goto settings.py and perform the following
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangodb1',
        'USER': 'root',
        'PASSWORD':'root'
    }
}
#----------------------------------------------------------------------------------------------------
#Step 7:
(venv) C:\Users\DELL\PycharmProjects\myproj17>pip install mysqlclient

#----------------------------------------------------------------------------------------------
#Step 8:
Tools----->Run manage,py Task

#----------------------------------------------------------------------------------------------------
#Step 9:makemigrations
(venv) C:\Users\DELL\PycharmProjects\myproj17>py manage.py makemigrations
Migrations for 'FormDBApp':
  FormDBApp\migrations\0001_initial.py
    - Create model Product
#----------------------------------------------------------------------------------------------------
#Step 10:migrate
(venv) C:\Users\DELL\PycharmProjects\myproj17>py manage.py migrate
#---------------------------------------------------------------------------------------------------
#Step 11: Start the server and give req in the browser

http://127.0.0.1:8000/

Enter the pid:
Enter the ProductName:
Enter the productCost:
Enter the mfd:
Enter the Expdt:


mysql> use djangodb1;
Database changed
mysql> show tables;
+----------------------------+
| Tables_in_djangodb1        |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
| formdbapp_product          |
| salesapp_sales             |
+----------------------------+
12 rows in set (0.04 sec)

mysql> select * from formdbapp_product;
+-----+---------+-----------+------------+------------+
| pid | pname   | pcost     | pmfd       | pexpdt     |
+-----+---------+-----------+------------+------------+
| 101 | LG      |    3.2000 | 2019-12-21 | 2020-03-12 |
| 102 | Sony    |    3.2000 | 2019-10-21 | 2020-04-12 |
| 103 | Samsung | 3000.2000 | 2019-08-14 | 2020-05-12 |
+-----+---------+-----------+------------+------------+
3 rows in set (0.00 sec)

======----------------------------------------------------------------------------------------------
Taking the data from the database table and displying on the browser

for this we use modelAPI

syntax:
    modelname.objects.all()-------->it will read all the records from the database table
    and stores the data into one object.

for a partial rcord

def display(request):
    rec=product.
    objects.filter(pid=1002)
database table records represented object, we  cam forward to template

#witin the template by using django template scripting , we can read one by one recordfrom the
object and we can embed that recods into html page

No changes in
1)model class
2modelform class
3urls

------------------------------------------------------------------------------------------------------
open views.py and and perform the following 
from django.shortcuts import render
from .forms import ProductForm
from .models import Product
def input(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'links.html')  #add this
    else:
        form = ProductForm()
    return render(request, 'base.html', {'form': form})
def display(request):
    recs=Product.objects.filter(pid=1001)
    return render(request,'display.html',{'records':recs})

-----------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------
goto templates and create display.html

<html>
<body bgcolor="#00ffff">
<table border="1">
<tr >
  <th>pid</th>
  <th>pname</th>
  <th>pcost</th>
    <th>pmfd</th>
    <th>pexpdt</th>
</tr>
{% for rec in records %}
<tr>
  <td>{{ rec.pid }}</td>
  <td>{{ rec.pname }}</td>
  <td>{{ rec.pcost }}</td>
<td>{{ rec.pmfd }}</td>
<td>{{ rec.pexpdt }}</td>
</tr>
{% endfor %}
</table>
<a href="formdbapp">clck here to insert another product</a>
</body>
</html>


-------------------------------------------------------
create links.html in templates

<html>
<body>
<a href="./display">click here to display products</a>
</body>
</html>

----------------------------------------------------------------------------
goto urls.py and add one line as follows

from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from FormDBApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^formdbapp',views.input),
    url(r'^display$',views.display)
]


-----------------------------------------------------------------------------------------
migrate FormDBApp

start server-------->give request

http://127.0.0.1:8000/formdbapp

Enter product details

submit----------->displays product details------>click here to insert another product

























