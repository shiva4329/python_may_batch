
Regular Expressions:
    Regular Expressions are used for
    1)Extracting the required data from the given data or string
    2)To perform data validations
    3)To develop url patterns in the web application.

    

ex:101,smith,10000
   Blake,102,20000
   30000,103,miller
   
   Here i want to extract only names and print them
   so read each line from a file using file handling
   the line will be divided into multiple words,
   at 2nd location, name is available,
   I can't apply split(",") based on comma bcoz
   in 2nd line,name is in 1st location and in
      3rd line ,name is in 3rd location.
    so for this we go for Regular expression.



    
ex2:whenever we give request for a web appln, it searches for
    Url pattern
    if 1000 web pages ------->1000 url patterns are required,
    so it takes lot of time for searching
    so use R.E,
    for 1000webpages------>only 100 urls are enough
    for 100webpages------->only one url is enough
    use R.E,so it takes less time for searching

----------------------------------------------------------------------------------------------------   

In R.E's,we use some special characters to define the patterns,
after defining the patterns,we can extract that pattern mactching
data from the given data,by using pre-defined functions of RE module.

-re is a in-built module of python.

The following are some special characters used to define the patterns.

1)* : It matches with zero or more occurences of preceeding character

  ex: ab*c
           here the preceeding character is b,
     the above RE matches with the following
     ac
     abc
     abbc
     abbbc
     abbbbc
     
ex: (hello)* world

     world
     hello world
     hellohello world
--------------------------------------------------------------------------
2)+ : It matches with one or more occurences of preceeding character.
  ex: ab+c
           here preceeding character is b
      The above RE matches with the following          
      abc
      abbc
      abbbc
      abbbbc
      abbbbbc
      ac----->invalid
    
---------------------------------------------------------------------------
3)? : It matches with zero or one occurence of preceeding character
   ex: ab?c
       the RE matches with the following
       ac
       abc
       abbc---->invalid
   ex:2
       pea?rl
       matches with
       perl
       pearl
   ex:3
       colou?r
       matches with
       color
       colour
-----------------------------------------------------------------------------        
4). : It matches with any single character
   ex: a.c
       matches with
       agc
       a5c
       a$c
       a c
       adc
----------------------------------------------------------------------------
5)[ ]:It matches with any single character in the given list,
    ex:  b[aeiou]d
          all these character(a,e,i,o,u) can be present b/w b and d such as
          bad
          bed
          bid
          bod
          bud
          b8d---->invalid
          bpd---->invalid
-----------------------------------------------------------------------------
6)[^]:It matches with any single character other than in the given list
    ex:  b[^aeiou]d
          other than these characters(a,e,i,o,u),any character can be
          b/w  b and d  such as
          b8d---->valid
          bpd---->valid
          bad---->invalid
          bed---->invalid
          bid---->invalid
          bod---->invalid
          bud---->invalid
------------------------------------------------------------------------------
7)[-]:It matches with any single character in the given range
    ex:  x[a-e]y
             the range is from a to e
         matches with the following
         xay
         xby
         xcy
         xdy
         xey
         xfy---->invalid
         xpy---->invalid
    ex:2
        [0-9]--------->any single digit
        [a-z]--------->any one lowercase alphabet
        [A-Z]--------->any one uppercase alphabet
        [a-zA-Z]------>any one alphabet
        [a-zA-Z0-9_]-->any one alpha numeric,underscore also allowed
        [^0-9]-------->any single non digit.
        [^a-z]-------->any one non lowercase alphabet
        [^A-Z]-------->any one non uppercase alphabet
        [^a-zA-Z]----->any one non alphabet
        [^a-zA-z0-9_]-->any one non alphanumeric (special characters)

-----------------------------------------------------------------------------------
8) (|):match with any one string in the list.
    ex:(java|C|python)

------------------------------------------------------------------------------------
9){m}: It matches with exact occurence of preceeding character.
  ex: ab{3}c
             matches with exactly 3 occurence of b such as
      abbbc
      abbc--->invalid
      abbbbbbbc-->invalid

-----------------------------------------------------------------------------------
10)^---->xoR--->start of the line
    ex: ^perl
        ^[abc]
        ^[^abc]
-----------------------------------------------------------------------------------
11)$ :end of the line
    ex:  perl$
         [0-9]$
-----------------------------------------------------------------------------------
12)\d or [0-9] --->any single digit


   Representing 4 digit number: 
    [0-9][0-9][0-9][0-9]
             (or)
          [0-9]{4} #means the preceeding character[0-9] occurs for 4 times
             (or) 
        \d\d\d\d
              (or)
        \d{4}  #preceeding character occurs for 4 times
----------------------------------------------------------------------------------
13)\D or [^0-9]----->any single non digit

14)\w or [a-zA-Z0-9_]---->any alphanumeric

15)\W or [^a-zA-Z0-9_]----->any non alphanumeric or special character.

16)\s----->' ','\t','\n' i.e space,tabspace and newline
-----------------------------------------------------------------------------------------
examples:
    1.  JAN 15,MARCH 05,APRIL 16
        here JAN,MARCH,APRIL all are strings(non-numeric)
        15,05,16 are numeric means--->[0-9]{2} or \d{2}
        before numeric space--->' '
        so [a-zA-Z]*----->means 0 or more occurences
                          but i dont want 0 occurence
        so finally
        [a-zA-Z]+ ' ' [0-9][0-9]
      ex: JAN    space numeric
re is a pre-defined module,which has functions or methods for
Regular expressions















    


    
   

        


        




            

        






         
         
          
          
          







       






       







      
      




      








     




    
    
