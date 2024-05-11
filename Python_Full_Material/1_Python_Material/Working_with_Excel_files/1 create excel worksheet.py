

#Creating Excel files with Python and xlsxwriter
#xlsxwriter is a Python module for creating Excel XLSX files.

#pip install xlsxwriter

#Note :xlsxwriter can only create new files. It cannot read or modify existing files.

import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('studentmarks.xlsx')  #create a new workbook object using the Workbook() constructor
worksheet = workbook.add_worksheet() #Workbook() constructor takes one argument which is the filename that we want to create:
#The workbook object is then used to add a new worksheet via the add_worksheet() method:
# Start from the first cell. Rows and columns are zero indexed.
row = 1
col = 0
#By default worksheet names in the spreadsheet will be Sheet1, Sheet2 etc., but we can also specify a name:
# Some data we want to write to the worksheet.
worksheet.write('A1','Subject')
worksheet.write('B1','Marks')

details = (
    ['English', 75],
    ['Maths',   95],
    ['Physics',  60],
    ['Chemistry', 85]
)

# Iterate over the data and writing row by row.
for subject, marks in (details):
    worksheet.write(row, col,subject) #We can then use the worksheet object to write data via the write() method:
    worksheet.write(row, col + 1, marks)
    row += 1

# Write a total using a formula.
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B5:B2)')

workbook.close()
