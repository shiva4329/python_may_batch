# Program to extract number of columns in Python 
import xlrd 
  
loc = ("F:/emp.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
sheet.cell_value(0, 0) 
  
# Extracting number of columns 
print(sheet.ncols) 
