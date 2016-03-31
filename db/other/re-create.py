# // procs remove themselves

# // tables
# source /home/applekey/Documents/LeetBros/db/tables/Bill_tbl.sql
# source /home/applekey/Documents/LeetBros/db/tables/User_tbl.sql
# source /home/applekey/Documents/LeetBros/db/tables/ClientSID_tbl.sql
# source /home/applekey/Documents/LeetBros/db/tables/Template_tbl.sql


# // procs

# source /home/applekey/Documents/LeetBros/db/procs/uspAddUser.sql
# source /home/applekey/Documents/LeetBros/db/procs/uspCreateBill.sql
# source /home/applekey/Documents/LeetBros/db/procs/uspIfUserExists.sql
# source /home/applekey/Documents/LeetBros/db/procs/uspGetUserId.sql
# source /home/applekey/Documents/LeetBros/db/tables/uspAddTemplate.sql

# // sample data

import os, subprocess

def reCreateTxt():
	curDir = os.getcwd()
	dbDir = os.path.dirname(curDir)
	tableDir = os.path.join(dbDir, 'tables')
	procDir = os.path.join(dbDir, 'procs')

	allSqlFile = 'all.sql'

	catString = 'cat ' 

	## tables
	for filename in os.listdir(tableDir):
		if filename.endswith('.sql'):
			catString += os.path.join(tableDir, filename) + ' '

	## porcs
	for filename in os.listdir(procDir):
		if filename.endswith('.sql'):
			catString += os.path.join(procDir, filename) + ' '

	## sample data
	catString += os.path.join(curDir, 'sampleData.sql') + ' '

	catString += ' >' +allSqlFile

	print catString 
reCreateTxt()




