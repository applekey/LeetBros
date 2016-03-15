from include import *
import datetime
## bill tests
def insertBillTest():
	bAdapter = billAdapter(*dbManager.getDBConfig())

	data = {
			'Name': 'ef',
			'Description':'fda',
			'Amount':6,
			'DueDate':str(datetime.datetime.now()),
			'BillIssuerId':'6df8ca38-ea38-11e5-a609-f7c4ee5bfee6',
			'BillPayeeId':'6df8ca38-ea38-11e5-a609-f7c4ee5bfee6'}
	bAdapter.connect()
	#bAdapter.insertBill(data)
	print bAdapter.queryBills()
	bAdapter.disconnect()	

#insertBillTest()

def insertUserTest():
	usrAdapter = userAdapter(*dbManager.getDBConfig())
	usrAdapter.connect()

	data = {
	        'email' : "gmail.fcom",
	        'loginName' : "applekey",
	        'passord' : "vancouver!@#",
	        'firstName' : "Vincent",
	        'lastName': "Chen",
	        'groupId': '76af103c-ea3e-11e5-a609-f7c4ee5bfee6',
	        'userType': 3}
	    	

	#print userAdapter.queryUserByEmail("gmail.fcom")

	print usrAdapter.insertUser(data)

	usrAdapter.disconnect()
insertUserTest()

