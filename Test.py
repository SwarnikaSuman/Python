import xlsxwriter

a=0
b=1
workbook = xlsxwriter.Workbook("D:\python practice\printno.xlsx")
worksheet = workbook.add_worksheet()
worksheet.write(0,0,a)
worksheet.write(1,0,b)
for i in range(2,98):
    c=a+b
    b=c
    a=b
    worksheet.write(i,0,a)
    worksheet.write(i+1,0,b)
    worksheet.write(i+2,0,c)
workbook.close()
