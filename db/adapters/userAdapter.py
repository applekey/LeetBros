from dbAdapter import *

class userAdapter(dbAdapter):
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

    def insertUser(self, data):
        cursor = None
        try:
            uuid = None
            cursor = self.connection.cursor()
            if cursor is not None:
                args = (data['email'], data['loginName'], data['passord'], data['firstName'], data['lastName'],data['userType'])
                print args
                cursor.callproc('uspAddUser',args)
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