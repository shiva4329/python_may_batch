

python communication with mysql database:

To provide connection b/w python program and mysql database,

we require a external  module called "pymysql",
we need to download and install it  using pip.

installing pymysql module:

goto cmdprompt and---> goto python installed folder and in that, we have a
folder called scripts, in that folder pip is available. 
C:\Users\DELL>cd\

C:\>cd Python37

C:\Python37>cd Scripts

C:\Python37\Scripts>pip install pymysql
Note:internet is required to install this.

pip downloads and installs pymysql module,for connecting with mysql
now we can import pymysql module in our program

Note: If pymysql module is not installing ,then we have to install
      "microsoft visual c++ s/w "
    from google----> download "microsoft visual c++ for python 3.7" and install

    Even after installing "microsoft visual c++", still you get error in
    installing pymysql module, then work with old version,python 2.7,
    bcoz still they should not have updated

       (or)

   #To check whether it is working or not
   open interpreter >>>and type---> import pymysql ,it should not give any error
   or unidentified,it gives a blank line

To connect to database,we have a method called connect() of pymysql module and
it takes database details as parameters and connects to database such as
1.local host /ip address
2.Database Username
3.Database password










    
