from include import *
attachmentDirectory = os.path.join(os.getcwd(),'services')
sys.path.append(attachmentDirectory)
from serviceInclude import *
from datetime import datetime, date, time
from templateAdapter import *
from sendGridAdapter import *  
from templateEngine import * 


def testGetColumnValueIfExistsForClient():
	tAdapter = templateAdapter(*dbManager.getDBConfig())
	tAdapter.connect()
	print tAdapter.GetColumnValueIfExistsForClient('TemplateText','204de18f-ed4f-11e5-8824-8c89a5c59145')
	tAdapter.disconnect()
testGetColumnValueIfExistsForClient()

def testTemplateEngine():

	text = 'simply dummy $userAttribute text of the printing and typesetting'
	text+= ' industry. Lorem Ipsum has been the industr'
	clientId = 'dummyClientId'

	tEngine = templateEngine()
	tEngine.replace(text,clientId)


#testTemplateEngine()

def testCheckIfColumnExists():
	tAdapter = templateAdapter(*dbManager.getDBConfig())
	tAdapter.connect()
	print tAdapter.checkIfColumnExists('abcd')
	print tAdapter.checkIfColumnExists('description')
	tAdapter.disconnect()

#testCheckIfColumnExists()

#template tests
def testEmail():
	apiKey = 'SG.d8TGGDj-Tv6uKEGausdKEw.6eysJGilzT7Wlx36wTR6s2ZKaJ-n8uVNeSmu-e6eSgo'

	sgA = sendGridAdapter(apiKey)

	data = {
			'to': 'applekey@gmail.com',
			'from': 'applekey@gmail.com',
			'subject' : 'dummy html webpage',
			'text': 'email'
	}

	sgA.sendEmail(data)


#testEmail()



def testTemplates():
	print 'here'
	tAdapter = templateAdapter(*dbManager.getDBConfig())

	tAdapter.connect()

	clientId = '204de18f-ed4f-11e5-8824-8c89a5c59145'

	data = {
			'name': 'dummyTemplate',
			'description': 'dummyTemplateDescription',
			'templateText' : 'dummy html webpage',
			'createDate': str(datetime.now()),
			'creator':clientId
	}

	tAdapter.StoreTemplate(data,clientId)	

	print tAdapter.ListAvaliableTemplates(clientId)	
	tAdapter.disconnect()


#testTemplates()


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
#insertUserTest()

def querryPastBillsTest():
	bAdapter = billAdapter(*dbManager.getDBConfig())

	bAdapter.connect()
	#bAdapter.insertBill(data)
	print bAdapter.querryUpCommingBills()
	bAdapter.disconnect()
	
#querryPastBillsTest()

def DashTest():
	print GetDashInfo('blah','blah')

#print DashTest()

