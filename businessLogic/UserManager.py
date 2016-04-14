from userAdapter import *
from dbManager import *

class UserManager:
    def createUser(self, data):
        (username,password,host,database) = dbManager.getDBConfig()
        
        #try:
        args = {
        'email':data['email'],
        'loginName':data['email'],
        'passord':data['passw'],
        'firstName':data['firstName'],
        'lastName':data['lastName'],
        'groupId':1, #data['groupId']
        'userType':1 #data['userType']
        }
        usrAdapter =userAdapter(username,password,host,database)
        usrAdapter.connect()
        userExist = usrAdapter.insertUser(args)
        usrAdapter.disconnect()
        # except Exception, e:
        #     print 'createUser: ' + str(e)
        #     return False
        # return True