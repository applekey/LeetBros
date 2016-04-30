from dbAdapter import *
from datetime import datetime, date, time
class billAdapter(dbAdapter):

    def __init__(self, username,password,host,database):
        super(billAdapter, self).__init__(username,password,host,database)
        self.dbName = 'bill'

    def insertBill(self, data):
        cursor = None
        try:
            cursor = self.connection.cursor()
            args = (data['Name'], data['Description'], data['Amount'], data['DueDate'], data['BillIssuerId'], data['BillPayeeId'], data['Paid'], data['PaidDate'])
            cursor.callproc('uspCreateBill',args)
            self.connection.commit()

        except Exception, e:
            #log this failure
            print "error: userAdapter InsertBill: " + str(e)
            return False
        finally:
            if cursor != None:
                cursor.close()

    def queryBills(self, clientId):
        #print 'clientId: ' + str(clientId)
        query = "SELECT Name, Description, Amount, DATE_FORMAT(DueDate, '%d/%m/%Y') as DueDate from Bill where BillIssuerId = '{0}';".format(clientId)
        return self.simpleQueryRunner(query)


    def querryPastDueBills(self, billIssuerId = None, billPayeeId = None, limit = 0):

        query = "SELECT Name, Description, Amount, DATE_FORMAT(DueDate, '%d/%m/%Y') as DueDate from Bill where Paid = 1 and DueDate <= '{0}'".format(str(datetime.now()))

        if billIssuerId != None:
            # this is a user querry
            query += "and BillIssuerId = '{0}' ".format(billIssuerId)

        if billPayeeId != None:
            # this is a user querry
            query += "and billPayeeId = '{0}' ".format(billPayeeId)

        query += 'order by DueDate desc;'

        if limit > 0:
            query = query[:-1] # strip ';', will need a new one
            query += "limit = '{0}';".format(limit)

        result = self.simpleQueryRunner(query)
        print result
        return result

    def querryUpCommingBills(self, billIssuerId = None, billPayeeId = None, limit = 0):

        query = "SELECT Name, Description, Amount, DATE_FORMAT(DueDate, '%d/%m/%Y') as DueDate from Bill where Paid = 0 and DueDate > '{0}'".format(str(datetime.now()))

        if billIssuerId != None:
            # this is a user querry
            query += "and BillIssuerId = '{0}' ".format(billIssuerId)

        if billPayeeId != None:
            # this is a user querry
            query += "and billPayeeId = '{0}' ".format(billPayeeId)

        query += 'order by DueDate asc;'

        if limit > 0:
            query = query[:-1] # strip ';', will need a new one
            query += "limit = '{0}';".format(limit)

        result = self.simpleQueryRunner(query)
        print result
        return result

