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

    def insertUser(self, user, data):
        cursor = None
        try:
            cursor = self.connection.cursor()
            args = (data['email'], data['loginName'], data['passord'], data['firstName'], data['lastName'],data['userType'])
            uuid = cursor.callproc('uspAddUser',args)

            return uuid
        except Exception, e:
            #log this failure
            print "userAdapter queryUser: " + str(e)
            return -1
        finally:
            if cursor != None:
                cursor.close()