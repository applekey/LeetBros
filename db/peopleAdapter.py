from dbAdapter import *
class clientContainer:
    #this class contains the fields for clients
    self.name = None
    self.email = None

class peopleAdapter(dbAdapter):
    def querryClients(self):
        result = []
        cursor = self.connection.cursor()
        query = ("SELECT * FROM people_tbl;")
        cursor.execute(query)
        for curResult in cursor:
            result.append(curResult)
        cursor.close()
        return result

    def createClient(self, clientContainer):
        cursor = None
        clientData = (clientContainer.name,clientContainer.email)
        try:
            cursor = self.connection.cursor() 
            query = ("INSERT INTO people_tbl ('people_name','people_email') values(%s, %s)") 
            cursor.execute(query,clientData)
            self.connection.commit()
            cursor.close()
        except:
            #log this failure
            pass
        finally:
            if cursor != None:
                cursor.close()
