import xlrd

workbook = xlrd.open_workbook('/Users/vanamali/PycharmProjects/pytestNaveen/data/DataFile.xls')
sheet1 = workbook.sheet_by_name('Sheet1')

# get number of rows
rowCount = sheet1.nrows
colCount = sheet1.ncols

print(rowCount)
print(colCount)

for curr_row in range(1, rowCount):
    userName = sheet1.cell_value(curr_row, 0)
    passWord = sheet1.cell_value(curr_row, 1)

    print(f"{userName} {passWord}")


'''
https://youtu.be/PQfTQ4QNZjA
'''