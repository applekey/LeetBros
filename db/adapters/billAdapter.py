from dbAdapter import *

class billAdapter(dbAdapter):

    def insertBill(self, data):
        cursor = None
        try:
            cursor = self.connection.cursor()
            args = (data['Name'], data['Description'], data['Amount'], data['DueDate'], data['BillIssuerId'], data['BillPayeeId'])
            cursor.callproc('uspCreateBill',args)
           
        except Exception, e:
            #log this failure
            print "userAdapter InsertBill: " + str(e)
            return False
        finally:
            if cursor != None:
                cursor.close()
   
    def queryBills(self):
        query = "SELECT bill_name, bill_description, bill_amount, DATE_FORMAT(bill_date, '%d/%m/%Y') as bill_date from bill_tbl;"
        return self.simpleQueryRunner(query)
