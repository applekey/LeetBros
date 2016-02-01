from dbAdapter import *

class billAdapter(dbAdapter):

    def insertBill(self, data):
    	cursor = None
        try:
            cursor = self.connection.cursor()
            query = ("""insert into bill_tbl(bill_name, bill_description, bill_amount, bill_date)
    					values ('{0}', '{1}', {2}, '{3}');
    				""".format(data['name'], data['desc'], data['amt'], data['date']))
            cursor.execute(query)
            self.connection.commit()
            return cursor.lastrowid
        except Exception, e:
            #log this failure
            print "bill adapter insertBill: " + str(e)
            return -1
        finally:
            if cursor != None:
                cursor.close()

    def queryBills(self):
        query = "SELECT bill_name, bill_description, bill_amount, DATE_FORMAT(bill_date, '%d %m %Y') as bill_date from bill_tbl;"
        return self.simpleQueryRunner(query)
