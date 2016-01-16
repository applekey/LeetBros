from dbAdapter import *
from peopleContainer import *

class peopleAdapter(dbAdapter):

    def __simpleQueryRunner(self, query):
        result = []
        cursor = self.connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        while row is not None:
            result.append(dict(zip(cursor.column_names, row)))
            row = cursor.fetchone()
        cursor.close()
        return result

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
        except:
            #log this failure
            print 'failure'
            return False
        finally:
            if cursor != None:
                cursor.close()

    def queryClients(self):
        query = ("SELECT people_name,people_email FROM people_tbl;")
        results = self.__simpleQueryRunner(query)
        clientResults = []
        for result in results:
            container = peopleContainer()
            container.initWithDB(result)
            clientResults.append(container)

        result = peopleContainer.seralizeToJsonList(clientResults)

        return result


    def queryOwed(self):
        query = "SELECT * from owed_tbl where paid = false;"
        return self.__simpleQueryRunner(query)

    def queryPaid(self):
        query = "SELECT * from owed_tbl where paid = true;"
        return self.__simpleQueryRunner(query)

    def queryUnpaidBills(self):
        query = "SELECT * from unpaidBills;"
        return self.__simpleQueryRunner(query)
