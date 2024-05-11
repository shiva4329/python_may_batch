#creating MYSQL DigitalNest databse using python scripting
import pymysql
con=pymysql.connect('localhost','root','43294329')
cur1=con.cursor()
cur1.execute('create database DigitalNest')
cur1.close()
con.close()
