'''
pip install pandas
main components of pandas are
i)Series
ii)DataFrame.

i)Series is nothing but a column
iiDataFrame is a multi-dimensional table made up of a collection of Series.

ex:
    series   series    DataFrame
      eid    ename     eid ename
      101    Miller    101 Miller
      102 +  Blake  =  102 Blake
      103    James     103 James
      104    John      104 John

'''
#-----------------------------------------------------------------------------------------------------
#Creating DataFrames


import pandas as pd
data={
      "enames":["Miller","Blake","James","John"],
      "sals":[10000,20000,30000,40000]
      }

#passing this data to pandas DataFrame Constructor , so that a dataframe gets created

df1=pd.DataFrame(data)
print(df1)
print("\n\n")
'''
o/p:
  enames   sals
0  Miller  10000
1   Blake  20000
2   James  30000
3    John  40000 '''
#Note here by default we get index starting with 0, even we can have our own index
 
#----------------------------------------------------------------------------------------------------
#ex:2 Even we can have index in string type

import pandas as pd
data={
      "Sony":[250,350,200,150,300],
      "LG":[300,180,260,200,150],
      "Lenovo":[300,180,260,200,150]
      }
df2 = pd.DataFrame(data, index=["April","May","June","July","August"])
print(df2)
'''
o/p:
        Sony   LG  Lenovo
April    250  300     300
May      350  180     180
June     200  260     260
July     150  200     200
August   300  150     150 '''
print("\n\n")
#Retrieving particular month data
print(df2.loc["April"])

print("\n\n")












