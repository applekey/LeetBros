import mysql.connector

class dbAdapter(object):
    # config = {
    #   'user': 'scott',
    #   'password': 'tiger',
    #   'host': '127.0.0.1',
    #   'database': 'employees',
    #   'raise_on_warnings': True,
    # }
    def __init__(self, username,password,host,database):
        self.username = username
        self.password = password
        self.host = host
        self.database = database
        self.connection = None
        self.dbName = None
        self.clientIdentifierColumnName = None

    def connect(self):
        self.connection = mysql.connector.connect(user=self.username, password=self.password,
                              host=self.host,
                              database=self.database)
                              #connector.connect(**config)

    def simpleQueryRunner(self, query):
        result = []
        cursor = self.connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        while row is not None:
            result.append(dict(zip(cursor.column_names, row)))
            row = cursor.fetchone()
        cursor.close()
        return result

############################################################################
############### Funcs that should rly be in inherited class, but too lazy to do that rit now
#######################################
    def GetColumnValueIfExistsForClient(self, columnName, clientId):
        if self.dbName == None:
            raise ValueError('db name is not set, this should be set when you override the class!!!')
            return False

        if self.clientIdentifierColumnName == None:
            raise ValueError('clientIdentifierColumnName name is not set, this should be set when you override the class!!!')
            return False

        if columnName == None:
            return False

        if clientId == None:
            return False

        cursor = self.connection.cursor()
        query = "show columns from {0} where field = '{1}';".format(self.dbName, columnName)
        print query
        cursor.execute(query)

        result = cursor.fetchone()
        
        if not result:
            cursor.close()
            return None
        
        query = "select {0} from {1} where {2} = '{3}';".format(columnName, self.dbName, self.clientIdentifierColumnName, clientId)
        row = cursor.fetchone()
        result = []
        result.append(dict(zip(cursor.column_names, row)))
        cursor.close()
        return result

    def checkIfColumnExists(self, columnName):
        if self.dbName == None:
            raise ValueError('db name is not set, this should be set when you override the class!!!')
            return False

        if columnName == None:
            return False

        cursor = self.connection.cursor()
        query = "show columns from {0} where field = '{1}';".format(self.dbName, columnName)
        print query
        cursor.execute(query)

        result = cursor.fetchone()
        cursor.close()

        if result:
            return True
        else:
            return False

    def disconnect(self):
        self.connection.close()

#######################################
################ end of lazy
