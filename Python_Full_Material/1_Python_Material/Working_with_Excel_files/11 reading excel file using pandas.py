#import pandas
from pandas import read_excel
# find your sheet name at the bottom left of your excel file and assign it to sheet_name
my_sheet = 'Sheet1'
file_name = 'emp.xlsx' # name of your excel file
df = read_excel(file_name, sheet_name = my_sheet) #dataframe gets created
print(df) # shows headers with  rows


