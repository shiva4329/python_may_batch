DJANGO :

-DJANGO is a open source web framework developed in python language and maintained by

 Django s/w Foundation"

-Django Framework is used to develop the web applications according to MVT pattern.

-MVT---->[Model-View-Template]



USer sends the request to the web application through the browser by typing URL or clicking on
hyperlinks or by submitting form

3 ways of sending request
1)submitting URL.
2)submitting form.
3)clicking hyperlink.

URL dispatcher : -URL dispatcher will take that URL and it will verify whether that URL is
                  valid or invalid.

                 -URL dispatcher verifies the given URL is valid (or) invalid by taking the
                  support of urls.py file

                 -Django Developer should provide all the URLs which are related to that
                  web application in urls.py file

                 -Internally Every url is linked with a function called view

                 -all these functions are defined in views.py file

                 urls.py ----------->contains  urls
                 views.py ---------->contains functions of urls.py file 

                 -if the user url is matching with anyone of the URL of urls.py file then
                  request will be forwarded to corresponding url linked view function
                  otherwise error message will be given to the user.
                   ex: error----> http404

view : view function receives the request object
       view process the request and gives the response in html file(Template)

       This template gets executed and gives response to browser as response object.

model: If database connection is not required then model is not required.
        then view directly gives data(response) to browser directly
        i.e view to template and template to browser.

------------------------------------------------------------------------------------------------------
pointS:
    
-Django is a open source ,can run on any server

-by default Django server comes along with Django software.
 even we can configure other servers explicitly such as tomcat and deploy our application  in it.
 
-and also a default database sqlite3 comes along with django s/w , but also we can configure
 our own databases

-input data is stored in request object 
-and this request object is stored as a parameter to view fn.
-output data is stored in response object.

-response can be in htmlfile,textfile,xmlfile,pdffile ,this should be specified
 in view function i.e in which format to display

-----------------------------------------------------------------------------------------------------

what internally happening in view:

-view takes the data from database and display the response to client based on user specified format.

-view process the request and stores the result in cache bcoz ,if second time the same request given
then we get the response faster as the result was stored in cache

-if different request is given again view process the request and stores it in cache.
 
-whenever view function is called, then internally view function will search for the cached version
 of requested web page.

-if cached version of the requested web page is found then immediately that webpage
 will be given to the client
 i.e if the requested webpage is not available in cache, then view function process the request

 processing the request means------>receiving the form data ,performing validations on the data,
 storing or retrieving data from the database through model objects.

After processing the request ,response can be given to the client in 2 ways
1)Giving the response directly to the client by storing the web page into the cache.
2)Giving the response to the client, through template by storing the webpage into the cache.

template is nothing but html file.

------------------------------------------------------------------------------------------------------
Django supports the "Django Template language" , which can be used in templates, to include the
dynamic data into the web page which HTML cannot do.

In Django template language , we can also write python code in it.
------------------------------------------------------------------------------------------------------

 
 








 












                 
