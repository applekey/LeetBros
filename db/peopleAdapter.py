from dbAdapter import *

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

    def queryClients(self):
        query = ("SELECT * FROM people_tbl;")
        return self.__simpleQueryRunner(query)

    def queryOwed(self):
        query = "SELECT * from owed_tbl where paid = false;"
        return self.__simpleQueryRunner(query)

    def queryPaid(self):
        query = "SELECT * from owed_tbl where paid = true;"
        return self.__simpleQueryRunner(query)
    
    def queryUnpaidBills(self):
        query = "SELECT * from unpaidBills;"
        return self.__simpleQueryRunner(query)