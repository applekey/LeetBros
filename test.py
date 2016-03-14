from include import *
import datetime
## bill tests
def insertBillTest():
	(user, pw, host, db) = dbManager.getDBConfig()
	print (user, pw, host, db)
	bAdapter = billAdapter(user, pw, host, db)

	data = {
			'Name': 'ef',
			'Description':'fda',
			'Amount':6,
			'DueDate':str(datetime.datetime.now()),
			'BillIssuerId':'6df8ca38-ea38-11e5-a609-f7c4ee5bfee6',
			'BillPayeeId':'6df8ca38-ea38-11e5-a609-f7c4ee5bfee6'}
	bAdapter.connect()
	bAdapter.insertBill(data)
	bAdapter.disconnect()	

insertBillTest()

def insertUserTest():
	(user, pw, host, db) = dbManager.getDBConfig()
	print (user, pw, host, db)
	userAdapter = userAdapter(user, pw, host, db)
	userAdapter.connect()

	data = {
	        'email' : "gmail.fcom",
	        'loginName' : "applekey",
	        'passord' : "vancouver!@#",
	        'firstName' : "Vincent",
	        'lastName': "Chen",
	        'userType': 3}
	    	

	print userAdapter.queryUserByEmail("gmail.fcom")

	#print userAdapter.insertUser(data)

	userAdapter.disconnect()

