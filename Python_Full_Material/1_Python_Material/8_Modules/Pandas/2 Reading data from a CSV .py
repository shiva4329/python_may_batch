#Reading data from CSV File
import pandas as pd

df = pd.read_csv('F:/student.csv')
print(df)

print("\n\n")


#To remove the index
df = pd.read_csv('F:\student.csv',index_col=0)
print(df)

print("\n\n")

