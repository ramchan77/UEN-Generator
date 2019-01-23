import time
import csv
import xlsxwriter
from xlutils.copy import copy
from xlrd import open_workbook

#input_file_name = raw_input("Enter The Input file Name (with csv Extention ): ")
start_year=input("Enter The Year : ")
start_year1=[int(d) for d in str(start_year)]
start_number=input("Enter The Starting Number : ")
##if len(str(start_number))==1:
##    start_series=str(start_year1[2])+'000'+str(start_number)
##if len(str(start_number))==2:
##    start_series=str(start_year)+'00'+str(start_number)
##if len(str(start_number))==3:
##    start_series=str(start_year)+'0'+str(start_number)
##if len(str(start_number))==4:
##    start_series=str(start_year)+str(start_number)
start_uen=start_number
temp=start_uen%10000
end_number=(start_uen-temp)+10000
#print 'Starting Registration Number Series : '+start_series
#print 'It Will Run Upto : '+str(end_number)
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
        if len(str(start_uen))==1:
            start_series='000'+str(start_uen)
        if len(str(start_uen))==2:
            start_series='00'+str(start_uen)
        if len(str(start_uen))==3:
            start_series='0'+str(start_uen)
        if len(str(start_uen))==4:
            start_series=str(start_uen)
        digits=[int(d) for d in str(start_series)]
        digits_value=(18*15)+(start_year1[2]*14)+(start_year1[3]*5)+(6*14)+(3*21)+(digits[0]*13)+(digits[1]*2)+(digits[2]*5)+(digits[3]*18)
        digits_mod=digits_value%11
        alpha_value=digits_mod+1
        #print alpha_value
        if alpha_value==1:
            alpha_letter="A"
        if alpha_value==2:
            alpha_letter="B"
        if alpha_value==3:
            alpha_letter="C"
        if alpha_value==4:
            alpha_letter="D"
        if alpha_value==5:
            alpha_letter="E"
        if alpha_value==6:
            alpha_letter="F"
        if alpha_value==7:
            alpha_letter="G"
        if alpha_value==8:
            alpha_letter="H"
        if alpha_value==9:
            alpha_letter="J"
        if alpha_value==10:
            alpha_letter="K"
        if alpha_value==11:
            alpha_letter="L"
        if alpha_value==12:
            alpha_letter="M"
        if alpha_value==13:
            alpha_letter="N"
        if alpha_value==14:
            alpha_letter="P"
        if alpha_value==15:
            alpha_letter="Q"
        if alpha_value==16:
            alpha_letter="R"
        if alpha_value==17:
            alpha_letter="S"
        if alpha_value==18:
            alpha_letter="T"
        if alpha_value==19:
            alpha_letter="U"
        if alpha_value==20:
            alpha_letter="V"
        if alpha_value==21:
            alpha_letter="W"
        if alpha_value==22:
            alpha_letter="X"
        if alpha_value==23:
            alpha_letter="Y"
        if alpha_value==24:
            alpha_letter="Z"
        registration_number='T'+str(start_year1[2])+str(start_year1[3])+'FC'+str(start_series)+alpha_letter
##        print registration_number
##        sheet1.write(roww,coll,registration_number)
##        roww+=1
##        book.save(output_file_name)
        file.write(registration_number)
        file.write('\n')
        start_uen=start_uen+1
print 'Completed..'

