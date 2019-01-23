import time
import csv
import xlsxwriter
from xlutils.copy import copy
from xlrd import open_workbook

#input_file_name = raw_input("Enter The Input file Name (with csv Extention ): ")
start_year=input("Enter The Year : ")
start_number=input("Enter The Starting Number : ")
if len(str(start_number))==1:
    start_series=str(start_year)+'0000'+str(start_number)
if len(str(start_number))==2:
    start_series=str(start_year)+'000'+str(start_number)
if len(str(start_number))==3:
    start_series=str(start_year)+'00'+str(start_number)
if len(str(start_number))==4:
    start_series=str(start_year)+'0'+str(start_number)
if len(str(start_number))==5:
    start_series=str(start_year)+str(start_number)
start_uen=int(start_series)
temp=start_uen%50000
end_number=(start_uen-temp)+50000
print 'Starting Registration Number Series : '+start_series
print 'It Will Run Upto : '+str(end_number)
#end_url=input("Enter The Rabge Limit URL Count (just Enter The Integer ) : ")
output_file_name = raw_input("Enter The file Name  : ")
#print output_file_name
##workbook = xlsxwriter.Workbook(output_file_name)
##worksheet = workbook.add_worksheet()
##workbook.close()
##book_ro = open_workbook(output_file_name)
##book = copy(book_ro)
##sheet1 = book.get_sheet(0)
##count=0
##roww=0
##coll=0
with open(output_file_name+'.csv','wb') as file:
    for i in range(start_uen,end_number): 
        digits=[int(d) for d in str(start_uen)]
        digits_value=(digits[4]*1)+(digits[5]*2)++(digits[6]*3)++(digits[7]*4)+(digits[8]*5)++(digits[0]*6)++(digits[1]*7)++(digits[2]*8)++(digits[3]*9)
        digits_mod=digits_value%11
        alpha_value=11-digits_mod
        #print alpha_value
        if alpha_value==1:
            alpha_letter="C"
        if alpha_value==2:
            alpha_letter="D"
        if alpha_value==3:
            alpha_letter="E"
        if alpha_value==4:
            alpha_letter="G"
        if alpha_value==5:
            alpha_letter="H"
        if alpha_value==6:
            alpha_letter="K"
        if alpha_value==7:
            alpha_letter="M"
        if alpha_value==8:
            alpha_letter="N"
        if alpha_value==9:
            alpha_letter="R"
        if alpha_value==10:
            alpha_letter="W"
        if alpha_value==11:
            alpha_letter="Z"
        registration_number=str(start_uen)+alpha_letter
#        print registration_number
##        sheet1.write(roww,coll,registration_number)
##        roww+=1
##        book.save(output_file_name)
        file.write(registration_number)
        file.write('\n')
        start_uen=start_uen+1
print 'Completed..'

