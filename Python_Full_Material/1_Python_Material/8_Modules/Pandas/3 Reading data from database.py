#Reading data from a database using Pandas
import pandas as pd
import pymysql
db=pymysql.connect('localhost','root','root','mydb7')

df = pd.read_sql_query("SELECT * FROM EMP", db)
print(df)
