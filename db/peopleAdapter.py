from dbAdapter import *

class peopleAdapter(dbAdapter):

    def __simpleQueryRunner(self, query):
        result = []
        cursor = self.connection.cursor()
        cursor.execute(query)
        for curResult in cursor:
            result.append(curResult)
        cursor.close()
        return result

    def queryClients(self):
        query = ("SELECT * FROM people_tbl;")
        return self.__simpleQueryRunner(query)

    def queryOwed(self):
        query = "SELECT * from owed_tbl limit 100 offset 0;"
        return self.__simpleQueryRunner(query)
        