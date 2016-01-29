from dbAdapter import *

class owedAdapter(dbAdapter):

    def insertOwed(self, peopleId, billId):
    	cursor = None
        try:
            cursor = self.connection.cursor()
            query = ("""insert into owed_tbl(owed_people_id, owed_bill_id)
    					values ({0}, {1});
    				""".format(peopleId, billId)
    				)
            cursor.execute(query)
            self.connection.commit()
            #return cursor.lastrowid
        except Exception, e:
            #log this failure
            print "owedAdapter insertOwed: " + str(e)
            return -1
        finally:
            if cursor != None:
                cursor.close()