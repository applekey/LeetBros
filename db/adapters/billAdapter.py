from dbAdapter import *

class billAdapter(dbAdapter):

    def insertBill(self, data):
        cursor = None
        try:
            cursor = self.connection.cursor()
            args = (data['Name'], data['Description'], data['Amount'], data['DueDate'], data['BillIssuerId'], data['BillPayeeId'])
            cursor.callproc('uspCreateBill',args)
            self.connection.commit()
           
        except Exception, e:
            #log this failure
            print "userAdapter InsertBill: " + str(e)
            return False
        finally:
            if cursor != None:
                cursor.close()
   
    def queryBills(self):
        query = "SELECT Name, Description, Amount, DATE_FORMAT(DueDate, '%d/%m/%Y') as DueDate from Bill;"
        return self.simpleQueryRunner(query)
