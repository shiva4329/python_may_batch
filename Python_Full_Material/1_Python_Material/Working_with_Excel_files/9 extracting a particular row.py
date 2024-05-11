# Program to extract a particular row value 
import xlrd 
  
loc = ("F:/emp.xlsx")
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)

print(sheet.row_values(1)) 
