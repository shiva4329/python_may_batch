LoginandRegApp:

steps:
step1: model.py ------>create one model

step 2: forms.py------>2forms------>i)RegForm
                                    ii)LoginForm

step 3: views.py

step 4:home.html------------>2 anchor tags---->
                           i)<a href="./reg">
                          ii)<a href="./login>

step 5: 2 html files--------->i)registration.html
                              ii)login.html
step 6: urls.py file---------->3 urls---------> for------>i)home
                                                         ii)registration
                                                         iii)Login

step 7:settings.py----------->Database change from sqlite3-------->mysql

step 8:tools----------->manage.py-------->migrate LoginRegApp

step 9: makemigrations------>myproj19>py manage.py makemigrations

step 10: myproj19>py manage.py migrate

step 11:goto------------>Database and check the tables created

step 12: runserver....




