

# Program to extract all the rows 
import xlrd 
  
loc = ("F:/emp.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
#sheet.cell_value(0, 0)

for i in range(sheet.nrows): 
    print(sheet.row_values(i)) 
