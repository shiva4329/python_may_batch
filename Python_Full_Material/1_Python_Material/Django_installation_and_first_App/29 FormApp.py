

Form:

A Form is nothing but a python class which extends django.forms.form class

Form classes are used to develop re-usable html code.

-The attributes which are defined in the form class represent a one of the input field of html form

-whenever we use form class object in html file , automatically form attributes fields are created
 in html file

 -------------------------------------------------------------------------------------------------
 Create a Project
 project:myproj16
 Application Name: FormApp
 
#step 1: creating forms.py
         ->rightclick----->FormApp------>create new python file------>Name: forms.py

open forms.py and write the following code

from django import forms
class NameForm(forms.Form):
    your_name = forms.CharField(label='Enter Your name', max_length=100)

--------------------------------------------------------------------------------------------------
#step 2: Goto views.py and write the following code

from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponse
def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponse('thanks')
    else:
        form = NameForm()
    return render(request, 'base.html', {'form': form})

---------------------------------------------------------------------------------------------------
#step 3: goto Templates------>right click------>create base.html
#open base.html and write the following code

<html>
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
#step 4: urls.py file

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from FormApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.get_name)
]

-----------------------------------------------------------------------------------------------------
#step 5: Tools-------> run manage.py Task
        @migrate FormApp

-----------------------------------------------------------------------------------------------------
#step 6: Runserver and give request

Enter ur Name: Vijay

thanks..


















 
