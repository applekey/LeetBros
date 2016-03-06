from dbAdapter import *
from peopleContainer import *

class peopleAdapter(dbAdapter):
    def createClient(self, clientContainer):
        cursor = None
        clientData = (clientContainer.name,clientContainer.email)
        print clientData
        try:
            cursor = self.connection.cursor()
            query = ("INSERT INTO people_tbl (people_name,people_email) VALUES (%s, %s)")
            cursor.execute(query,clientData)
            self.connection.commit()
            cursor.close()
            return True
        except Exception, e:
            #log this failure
            print "ppl adapter createClient: " + str(e)
            return False
        finally:
            if cursor != None:
                cursor.close()

    def queryClients(self):
        query = ("SELECT people_name,people_email FROM people_tbl;")
        results = self.simpleQueryRunner(query)
        clientResults = []
        for result in results:
            container = peopleContainer()
            container.initWithDB(result)
            clientResults.append(container)
        result = peopleContainer.seralizeToJsonList(clientResults)
        return result

    def deleteClient(self,clients):
        try:
            cursor = self.connection.cursor()
            query = ("DElETE From people_tbl where people_email VALUES (%s, %s)")
            cursor.execute(query,clientData)
            self.connection.commit()
            cursor.close()
            return True
        except:
            #log this failure
            print 'failure'
            return False
        finally:
            if cursor != None:
                cursor.close()

    def queryClientByEmail(self, email):
        query = ("SELECT * FROM people_tbl WHERE people_email='{0}';".format(email))
        return self.simpleQueryRunner(query)[0]

    def queryUnpaidBills(self):
        query = "SELECT * from unpaidBills;"
        return self.simpleQueryRunner(query)
