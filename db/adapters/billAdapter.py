from dbAdapter import *
from datetime import datetime, date, time
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

    def queryBills(self, clientId):
        #print 'clientId: ' + str(clientId)
        query = "SELECT Name, Description, Amount, DATE_FORMAT(DueDate, '%d/%m/%Y') as DueDate from Bill where BillIssuerId = '{0}';".format(clientId)
        return self.simpleQueryRunner(query)


    def querryPastDueBills(self, billIssuerId = None, billPayeeId = None):

        query = "SELECT Name, Description, Amount, DATE_FORMAT(DueDate, '%d/%m/%Y') as DueDate from Bill where DueDate <= '{0}';".format(str(datetime.now()))

        if billIssuerId != None:
            # this is a user querry
            query = query[:-1] # strip ';', will need a new one
            query += "and BillIssuerId = '{0}';".format(billIssuerId)

        if billIssuerId != None:
            # this is a user querry
            query = query[:-1] # strip ';', will need a new one
            query += "and billPayeeId = '{0}';".format(billPayeeId)

        return self.simpleQueryRunner(query)

    def querryUpCommingBills(self, billIssuerId = None, billPayeeId = None):

        query = "SELECT Name, Description, Amount, DATE_FORMAT(DueDate, '%d/%m/%Y') as DueDate from Bill where DueDate > '{0}';".format(str(datetime.now()))

        if billIssuerId != None:
            # this is a user querry
            query = query[:-1] # strip ';', will need a new one
            query += "and BillIssuerId = '{0}';".format(billIssuerId)

        if billIssuerId != None:
            # this is a user querry
            query = query[:-1] # strip ';', will need a new one
            query += "and billPayeeId = '{0}';".format(billPayeeId)

        return self.simpleQueryRunner(query)

