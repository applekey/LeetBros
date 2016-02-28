from dbAdapter import *

class userAdapter(dbAdapter):
    def queryUser(self,user,password):
        cursor = None
        try:
            exist = 0
            cursor = self.connection.cursor()
            args = (user, password, 0)
            result_args = cursor.callproc('uspIfUserExists',args)

            return result_args[2]
        except Exception, e:
            #log this failure
            print "userAdapter queryUser: " + str(e)
            return -1
        finally:
            if cursor != None:
                cursor.close()

    def insertUser(self, user, password):
        pass