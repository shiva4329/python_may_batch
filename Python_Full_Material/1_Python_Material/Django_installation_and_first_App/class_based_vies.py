Class -based views
    
    --> not only function based views but can also class -based views also
   -->  any user defined class which is extending pre-defined class called django.views.generic.view class known as class based views.
   -->  within yhe class based views, we can define different httpmethods related logics in different methods.
   -->  in functon -based views , all http request related method logics can implemented in single view function by using conditional statements.
   --> in function based views dont support re-usability mechanisam.
   --> class based supports re-usability because in heritence possible between the classes.
   --> when ever GET request is forwarded to class-based views, then automatically get() method of that views class will be executed and gives the response to the client.
   --> when ever POST request is forwarded to the class-based views , then automatically post() method of that view class will be executted and gives the response to the client.
   --> how to register function based views into url ---- by using regular expressions.
   --> For class based vies we register as
           
           url(r'^urlpattern$',viewclassname.as_views())
           
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Step 1 : open views.py and write the below code
    
        from django.shortcuts import render
        from django.views.generic import View
        from django.http import HttpResponse

        # Create your views here.
        class input(View):
            def get(self,request):
                return render(request,'base.html')
        class Add(View):
            def post(self,request):
                x=int(request.POST['t1'])
                y = int(request.POST['t2'])
                z=str(x+y)
                return HttpResponse("<html><body> SUM ="+z+"</body></html>")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Step 2: open base.html and write the below code


        <html>
        <body>
        <form action="./Add" method="post">
            {% csrf_token %}
        Enter 1st number<input type="text" name="t1"><br>
        Enter 2nd number<input type="text" name="t2"><br>
            <input type="submit" value="Add">
        </form>
        </body>
        </html>
        
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Step 3 : open urls.py and write the below code


        from django.contrib import admin
        from django.urls import path
        from django.conf.urls import url
        from ClassBasedViewApp.views import *

        urlpatterns = [
            path('admin/', admin.site.urls),
            url(r'^$',input.as_view()),
            url(r'^Add$',Add.as_view())
        ]
        
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Step 4: open Tools --------------click -----> Run manage.py

Step 5: migrate ApplicationName

Step 6: Runserver


        

        


