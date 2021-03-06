from dbAdapter import *

class userAdapter(dbAdapter):
    def __init__(self, username,password,host,database):
        super(userAdapter, self).__init__(username,password,host,database)
        self.dbName = 'user'
        self.clientIdentifierColumnName = 'UserId'
        

    def queryUser(self,user,password):
        cursor = None
        try:
            exist = 0
            cursor = self.connection.cursor()
            args = (user, password, 0)
            result_args = cursor.callproc('uspIfUserExists',args)
            if result_args[2] != 1:
                return False
            else:
                return True
        except Exception, e:
            #log this failure
            print "userAdapter queryUser: " + str(e)
            return False
        finally:
            if cursor != None:
                cursor.close()


    def queryUserByClientId(self, clientId):
        #print 'clientId: ' + str(clientId)
        query = "SELECT  Email, LoginName, FirstName,lastName from User where GroupId = '{0}';".format(clientId)
        return self.simpleQueryRunner(query)
 
    def queryUser(self):
        # only for debugging, remove 
        query = "SELECT  Email, LoginName, FirstName,lastName from User;"
        result = self.simpleQueryRunner(query)
        return result

    def insertUser(self, data):
        cursor = None
        try:
            uuid = None
            cursor = self.connection.cursor()
            if cursor is not None:
                args = (data['email'], data['loginName'], data['passord'], data['firstName'], data['lastName'], data['groupId'],data['userType'])
                cursor.callproc('uspAddUser',args)
                self.connection.commit()
            else:
                print 'no cursor'

            return uuid
        except Exception, e:
            #log this failure
            print "userAdapter insertUser: " + str(e)
            return -1
        finally:
            if cursor != None:
                cursor.close()