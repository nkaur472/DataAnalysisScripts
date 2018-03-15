'''
*** This script is reading data from two different sheets under same workbook.
 	This code is comparing data of provided column value from two different sheets.
 	The goal of this script was to prove the Y column is subset of X. ***


'''


import xlrd
import re


def ReadExcel(path,col,sheet,rb):
	IDsInTable = set()
	print (path+" "+str(col)+" "+str(sheet))
	rs = rb.sheet_by_index(sheet)
	s_col=''
	count =0
	for row in range(2,rs.nrows):

		# excel use float as default data type for numbers
		value = str((rs.cell_value(row,col)))
		
		# the returned number format is XXXXXXXX.0, matching the first group XXXXXXXX using regular expression  
		m = re.match(r'(^[0-9]+)',value)

		#checking for blank cells
		if m is not None:
			count += 1
			IDsInTable.add(m.group(0))
	print(count)
	return IDsInTable;


if __name__ == "__main__":

	# provide value of column from which data to be read
	col = 5;
	
	# path where excel file is store
	path_files = r"C:\Data\AVISvsRIP\AVISWithoutMatchingRIP.xlsx"
	
	# loading workbook in memory
	rb = xlrd.open_workbook(path_files)
	
	# creating set for data from AVIS
	AvisSet = ReadExcel(path_files,col,1,rb);

	# creating set for data from VIP 
	VipSet = ReadExcel(path_files,col,0,rb);

	# returning the diff between two sets of data
	diff = AvisSet.difference(VipSet)

	# converting the returned set into list
	difflist = list(diff)

	# provide name of file where data needs to be printed 
	text_file = open("UnmatchedAVIS2017.txt","w")
	for dlist in difflist:
		text_file.write(dlist+"\n")
	text_file.close()
	
