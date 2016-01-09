from dbAdapter import *

class peopleAdapter(dbAdater):
    def querryClients(self):
        result = []
        cursor = self.connection.cursor()
        query = ("SELECT * FROM people_tbl")
        cursor.execute(query)
        for curResult in cursor:
            result.append(curResult)
        cursor.close()
        return result
