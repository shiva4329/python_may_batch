
Create a Project
 project:myproj17
 Application Name: FormDBApp

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
from django import forms

class ProductForm(forms.Form):
    pid=forms.IntegerField(label="Enter the pid")
    pname=forms.CharField(label="Enter the ProductName:",max_length=100)
    pcost=forms.DecimalField(label="Enter the pCost",max_digits=100,decimal_places=9)
    pmfd=forms.DateField(label="Enter the mfd:")
    pexpdt=forms.DateField(label="Enter the Expdt:")

#---------------------------------------------------------------------------------------------------
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
            p=Product(pid=form.cleaned_data['pid'], #now storing the data of form class object into model class object(p)
                      pname=form.cleaned_data['pname'], #and wesave the model class object(p) data to database by saying p.save()
                      pcost=form.cleaned_data['pcost'],
                      pmfd=form.cleaned_data['pmfd'],
                      pexpdt=form.cleaned_data['pexpdt'])
            p.save()
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



